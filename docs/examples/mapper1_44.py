#-------------------------------------------------------------------------------
# Name:        mapper.py
# Version:     1.44
# Purpose:     Make maps of various weather parameters
# Author:      mike.callahan
# Modified:    11/13/2017
# History:     1.00 - inital version
#              1.01 - change output paths for NIDS server
#              1.02 - change spins for updated EzDialog
#              1.10 - include lsr option in snowd
#              1.20 - include lsr option in wind_gust
#              1.21 - cleanup code
#              1.30 - add KY accum map, add Louisville Metro maps
#              1.40 - add LSR tab, add state to snow maps, move status messages
#                     to new text window
#              1.41 - change output in input paths for cifs, save a copy of KMLs
#                     locally
#              1.42 - fix snow problems, cleanup code
#              1.43 - add KY state map to lSR
#              1.44 - fix add lsr to wind gust, add lsr to routine
# -------------------------------------------------------------------------------

import ezdialog, datetime, csv2kml, os, shutil, subprocess, catcsv

# version
VERSION = '1.44'

# directories
WORKSPACE  = 'c:\\gis\\Interpolations\\'
TEMPLATES  = 'c:\\gis\\Templates\\'
LDADINPUT  = r'\\204.194.228.10\cifs\AwipsToLan'
NIDSOUTMAP = r'\\204.194.228.10\cifs\NIDS\outbound\cms_images'
NIDSOUTKML = r'\\204.194.228.10\cifs\NIDS\outbound\cms_publicdata+kml'
KMLARCHIVE = 's:\\KMLArchive'

# ArcGIS files
WFO_SHP = 'CWA_Counties.shp'
KY_SHP  = 'Kentucky.shp'
SP_REF  = 'CWA_Counties.prj'
ROULOU  = 'loumetroprecip.mxd'
ROUWFO  = 'precip_2.mxd'
ROUKY   = 'KYpcpn_2.mxd'
ACCLOU  = 'accumLOUpcpn.mxd'
ACCWFO  = 'accumpcpn.mxd'
ACCKY   = 'accumKYpcpn_2.mxd'
TEMPSUF = '_temps.mxd'
SNOWWFO = 'snowdepth.mxd'
SNOWKY  = 'KYsnow.mxd'
WINDWFO = 'windgust.mxd'
LSRWFO  = 'lsr.mxd'
LSRKY   = 'kylsr.mxd'

# KML files
KMLCFG = ('pcpn','snowd','maxt','mint')

# catcsv CFG file
CATPCPN   = 'catpcpn.cfg'
CATSNOWD  = 'catsnowd.cfg'
COPYSNOWD = 'cpysnowd.cfg'
CATWIND   = 'catwind.cfg'

# commands
PNGVIEW = r'c:\Windows\system32\mspaint.exe'
CSVVIEW = r'c:\Program Files (x86)\Microsoft Office\Office14\excel.exe'

# tasks
types = {'Precipitation':'pcpn', 'Snow Depth':'snowd', 'Maximum':'maxt',
    'Minimum':'mint'}

class Gui(object):
    """ the GUI for the script """
    def __init__(self, mapper):
        self.mapper = mapper
        self.dialog = ezdialog.EzDialog()
        self.dialog.setTitle('Mapper ' + VERSION)
        self.pageHeaders = ['Routine', 'Accumulate', 'Temperature', 'Snow Depth',
            'Wind Gust', 'LSR']
        self.notebook, page = self.dialog.makeNotebook(0, self.pageHeaders)
        today = datetime.date.today()
        self.dt = today.strftime('%d,%m,%Y,%B').split(',')
        # routine page
        self.routine = ezdialog.EzDialog(page[0])
        self.routine.makeEntry(0, 60, 'Title', 10)
        self.routine[0] = '24 Hour Precipitation Ending 7 AM {0[3]} {0[0]}, {0[2]}'.format(
            self.dt)
        self.routine.makeEntry(1, 20, 'Output Filename', 10)
        self.routine[1] = 'pcpn{0[1]}{0[0]}{0[2]}.png'.format(self.dt)
        jobs = ['Make KMLs', 'Make Maps', 'Include LSRs']
        self.routine.makeChecks(2, 15, 'Jobs', jobs, 10)
        self.routine[2] = jobs[:2]
        self.routine.grid(padx=60)
        # accum pcpn page
        self.accum = ezdialog.EzDialog(page[1])
        parms = [1, 12, 1], [1, 31, 1], [2000, 2100, 2017]
        accumDate = self.accum.makeSpin(0, 4, 'Ending Date', parms, '/')
        self.accum[0] = [today.month, today.day, today.year]
        accumDate[0]['command'] = self.updateAccum
        accumDate[1]['command'] = self.updateAccum
        accumDate[2]['command'] = self.updateAccum
        accumBack = self.accum.makeSpin(1, 3, 'Days Back', [[1, 45, 2]], '', 10)
        accumBack[0]['command'] = self.updateAccum
        self.accum.makeEntry(2, 60, 'Title', 10)
        self.accum.makeEntry(3, 40, 'Output Filename', 10)
        self.updateAccum()
        self.accum.grid(padx=60)
        # temp page
        self.temp = ezdialog.EzDialog(page[2])
        tempType = self.temp.makeRadios(0, 10, 'Extremum', ['Maximum', 'Minimum'], 10)
        self.temp[0] = 'Maximum'
        tempType[0]['command'] = self.updateTemp
        tempType[1]['command'] = self.updateTemp
        self.temp.makeEntry(1, 60, 'Title', 10)
        self.temp.makeEntry(2, 40, 'Output Filename', 10)
        self.updateTemp()
        self.temp.grid(padx=60)
        # snow depth page
        self.snowd = ezdialog.EzDialog(page[3])
        self.snowd.makeEntry(0, 60, 'Title', 10)
        self.snowd[0] = 'Snow Depth Ending 7 AM {0[3]} {0[0]}, {0[2]}'.format(
            self.dt)
        self.snowd.makeEntry(1, 20, 'Output Filename', 10)
        self.snowd[1] = 'snowd{0[1]}{0[0]}{0[2]}.png'.format(self.dt)
        self.snowd.makeRadios(2, 26, 'Sources', ['Use Snow Depth', 'Use LSRs Only',
            'Merge LSRs into Snow Depth'], orient='vertical', gap=15)
        self.snowd[2] = 'Use Snow Depth'
        self.snowd.grid(padx=60)
        # wind gust page
        self.windg = ezdialog.EzDialog(page[4])
        self.windg.makeEntry(0, 60, 'Title', 10)
        hoursBack = self.windg.makeSpin(1, 3, 'Hours Back', [[1, 48, 6]], '', 10)
        hoursBack[0]['command'] = self.updateHours
        self.windg.makeEntry(2, 20, 'Output Filename', 10)
        self.windg[2] = 'windg{0[1]}{0[0]}{0[2]}.png'.format(self.dt)
        self.updateHours()
        self.windg.makeChecks(3, 12, 'Sources', ['Include LSRs'], 10)
        self.windg.grid(padx=60)
        # lsr page
        self.lsrg = ezdialog.EzDialog(page[5])
        self.lsrg.makeEntry(0, 60, 'Title', 10)
        self.lsrg.makeEntry(1, 20, 'Input Filename', 10)
        self.lsrg.makeEntry(2, 20, 'Output Filename', 10)
        self.lsrg[1] = 'lsr.csv'
        self.lsrg[2]= 'lsr{0[1]}{0[0]}{0[2]}.png'.format(self.dt)
        self.lsrg.grid(padx=60)
        # dialog
        self.notebook.grid()
        self.dialog.makeText(1, 70, 15, 'Messages', 3)
        buttons = self.dialog.makeButtons(2, space=20, gap=10)
        buttons[0]['command'] = self.go
        buttons[1]['text'] = 'Exit'
        self.dialog.grid()
        self.dialog[0] = 'Routine'

    def updateAccum(self):
        """ update widgets on accum page """
        end = self.accum[0]
        endDate = datetime.date(end[2], end[0], end[1])
        endDateFmt = endDate.strftime('%d,%m,%Y,%B').split(',')
        self.accum[2] = '{0} Day Precipitation Total Ending {1[3]} {1[0]}, {1[2]}'.format(
            self.accum[1][0], endDateFmt)
        begDate = endDate - datetime.timedelta(int(self.accum[1][0]) - 1)
        begDateFmt = begDate.strftime('%d,%m').split(',')
        self.accum[3] = 'accum{0[1]}{0[0]}-{1[1]}{1[0]}{1[2]}.png'.format(
            begDateFmt, endDateFmt)

    def updateHours(self):
        """ update widgets on wind gust page """
        self.windg[0] = '{0} Hour Highest Gust Ending 7AM {1[3]} {1[0]}, {1[2]}'.format(
            self.windg[1][0], self.dt)

    def updateTemp(self):
        """ update widgets on temp page """
        self.temp[1] = '{0} Temperature {1[3]} {1[0]}, {1[2]}'.format(self.temp[0],
            self.dt)
        tempType = 'maxt' if self.temp[0] == 'Maximum' else 'mint'
        self.temp[2] = '{1}{0[1]}{0[0]}{0[2]}.png'.format(self.dt, tempType)

    def addMessage(self, message):
        self.dialog[1] = message

    def go(self):
        """ get current selected page workaround """
        run = self.dialog[0]               # get selected tab
        if self.dialog.result:
            try:
                mapper = self.mapper(self)
                if run == 'Routine':
                    mapper.runRoutine()
                elif run == 'Accumulate':
                    mapper.runAccum()
                elif run == 'Temperature':
                    mapper.runTemp()
                elif run == 'Snow Depth':
                    mapper.runSnowd()
                elif run == 'Wind Gust':
                    mapper.runWindg()
                elif run == 'LSR':
                    mapper.runLsr()
            except:
                self.dialog[1] = self.dialog.catchExcept()

class Mapper(object):
    """ contain all GIS methods """

    def __init__(self, gui):
        """ create Mapper instance
            workspace:str - path to workspace
            gui: Gui object """
        self.gui = gui
        tdy = datetime.date.today()
        self.year, self.month, self.date, self.mnNum = tdy.strftime(
            '%Y,%b,%d,%m').split(',')               # get current date

    def makePlot(self, source, lon, lat, output):
        """ convert source to point shapefile
            source:str - source path
            lon:str - longitude field
            lat:str - latitude field
            output:str - point shapefile """
        self.gui.addMessage('Requesting ArcGIS from region, ')
        import arcview, arcpy
        self.arcpy = arcpy
        self.arcpy.env.workspace = WORKSPACE
        self.arcpy.env.overwriteOutput = True
        self.gui.addMessage('and making plot {}, '.format(output))
        layer = output.split('.')[0]                        # get shapefile name
        shutil.copy(source, WORKSPACE)                 # copy source to workspace
        fname = WORKSPACE+os.path.basename(source)          # get source filename
        spref = self.arcpy.SpatialReference(WORKSPACE+SP_REF) # get spatial reference
        self.arcpy.management.MakeXYEventLayer(fname, lon, lat, layer,
            spref)
        self.arcpy.management.CopyFeatures(layer, output)   # save layer as shapefile
        self.gui.addMessage('done.\n')

    def makeContour(self, source, col, mult, output):
        """ convert point shapefile to contoured polygon shapefile
            source:str - source point shapefile
            col:str - column name to contour
            mult:float - value to multiply to concern col to integer
            output:str - contoured polygon shapefile """
        self.gui.addMessage('Loading Spatial Analysis, ')
        if self.arcpy.CheckExtension('spatial') == 'Available':
            self.arcpy.CheckOutExtension('spatial')
        else:
            raise Error, 'Spatial Analysis not available, try 15 minutes later.'
        self.gui.addMessage('making contours, ')
        raster = self.arcpy.sa.Idw(source, col, 0.003, 2)
        temp = self.arcpy.sa.Int((raster * mult) + .5)
        self.arcpy.conversion.RasterToPolygon(temp, output, 'SIMPLIFY', 'VALUE')
        self.arcpy.CheckInExtension('spatial')
        self.gui.addMessage('done.\n')

    def makeKML(self):
        """ create the daily KMLs """
        self.gui.addMessage('Making KMLs, ')
        for cfg in KMLCFG:
            config = csv2kml.ConfigInfo(cfg+'k.cfg')
            self.gui.addMessage(config.check())
            kml = csv2kml.Kml(config.cfg, self.gui.addMessage)
            kml.write()
            path = '+{}+{}+'.format(self.year, self.month)
            fname = '{}_{}{}{}.kml'.format(cfg, self.mnNum, self.date, self.year)
            shutil.copy(cfg+'.kml', NIDSOUTKML+path+fname)
            shutil.copy(cfg+'.kml', '{}\\{}\\{}\\{}_{}{}{}.kml'.format(KMLARCHIVE,
                self.year, self.month, cfg, self.mnNum, self.date, self.year))
        self.gui.addMessage('done.\n')

    def makeClip(self, input, clipper, output):
        """ clip a layer
            input:str - input layer
            clipper:str - clipping layer
            output:str - output layer """
        self.gui.addMessage('Clipping layer to {}, '.format(output))
        self.arcpy.analysis.Clip(input, clipper, output)
        self.gui.addMessage('done.\n')

    def makePNG(self, mapDoc, title, png, width=82):
        """ export a mapdoc into an png
            mxd:MapDocument - ArcGIS map document
            title:str - Title of map
            png:str - path of PNG """
        self.gui.addMessage('Exporting to {}, '.format(png))
        mxd = self.arcpy.mapping.MapDocument(mapDoc)
        mxd.description = title.center(width)
        self.arcpy.mapping.ExportToPNG(mxd, png)
        self.gui.addMessage('done.\n')

    def joinLsr(self, config, dest):
        """ join or copy lsr into dest csv
            config:str - catcsv config filename
            dest:str - destination filename """
        if 'cat' in config:
            action = 'Merging'
        else:
            action = 'Copying'
        self.gui.addMessage('{} lsr.csv into {}, '.format(action, dest))
        cfg = catcsv.ConfigInfo(config)
        errors = cfg.check()
        if errors:
            self.gui.addMessage('Error in config: {}.\n'.format(errors))
        else:
            app = catcsv.Csvjoiner(cfg.cfg, self.gui.addMessage)
            app.write()
            self.gui.addMessage('done.\n')

    def runRoutine(self):
        """ make the routine precipitation maps """
        title = self.gui.routine[0]
        filename = self.gui.routine[1]
        actions = self.gui.routine[2]
        n = 1
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        if 'Include LSRs' in actions:
            self.joinLsr(CATPCPN, 'pcpn.csv')
            shutil.copy(LDADINPUT+'\\tpcpn.csv', LDADINPUT+'\\pcpn.csv')
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
        if 'Make KMLs' in actions:
            self.makeKML()
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
        if 'Make Maps' in actions:
            # make shapefiles
            self.makePlot(LDADINPUT+'\\pcpn.csv', 'lon', 'lat', 'pcpn.shp')
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
            self.makeContour('pcpn.shp', 'Pcpn', 100, 'pcpncontour.shp')
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
            self.makeClip('pcpncontour.shp', WFO_SHP, 'LMKprecip_clip.shp')
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
            self.makeClip('pcpncontour.shp', KY_SHP, 'KYprecip_clip.shp')
            # make PNGs
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
            wfopng = 's:\\Precip maps\\' + filename
            kypng = 's:\\Precip maps\\ky\\ky' + filename
            loupng = 's:\\Precip maps\\lou\\lou' + filename
            self.makePNG(TEMPLATES+ROUWFO, title, wfopng)
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
            self.makePNG(TEMPLATES+ROUKY, title, kypng)
            self.gui.addMessage('Step {}: '.format(n))
            self.makePNG(TEMPLATES+ROULOU, title, loupng)
            # copy to NIDS
            extloupng = '+LOUdaily+lou'+filename
            extwfopng = '+WFOdaily+'+filename
            extkypng = '+KYdaily+ky'+filename
            shutil.copy(loupng, NIDSOUTMAP+'+pcpn'+extloupng)
            shutil.copy(wfopng, NIDSOUTMAP+'+pcpn'+extwfopng)
            shutil.copy(kypng, NIDSOUTMAP+'+pcpn'+extkypng)
            # show maps
            self.gui.addMessage('All tasks completed, popping up viewers.\n\n')
            subprocess.Popen((PNGVIEW, wfopng))
            subprocess.Popen((PNGVIEW, kypng))
            subprocess.Popen((PNGVIEW, loupng))
            subprocess.Popen((CSVVIEW, LDADINPUT+'\\pcpn.csv'))

    def runAccum(self):
        """ make the accumulate precipitation map """
        title = self.gui.accum[2]
        filename = self.gui.accum[3]
        n = 1
        # make shapefiles
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makePlot(LDADINPUT+'\\accum_pcpn.csv', 'lon', 'lat', 'accumpcpn.shp')
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makeContour('accumpcpn.shp', 'Pcpn', 100, 'contour.shp')
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makeClip('contour.shp', WFO_SHP, 'LMKprecip_clip.shp')
        wfopng = 's:\\Precip maps\\accum precip\\' + filename
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makeClip('contour.shp', KY_SHP, 'KYprecip_clip.shp')
        kypng = 's:\\Precip maps\\accum precip\\ky\\ky' + filename
        # make PNGs
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makePNG(TEMPLATES+ACCWFO, title, wfopng)
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makePNG(TEMPLATES+ACCKY, title, kypng)
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        loupng = 's:\\Precip maps\\accum precip\\lou\\lou' + filename
        self.makePNG(TEMPLATES+ACCLOU, title, loupng)
        # copy to NIDS
        extloupng = '+LOU+lou'+filename
        extwfopng = '+WFO+'+filename
        extkypng = '+KY+ky'+filename
        shutil.copy(wfopng, NIDSOUTMAP+'+pcpn+accum'+extwfopng)
        shutil.copy(kypng, NIDSOUTMAP+'+pcpn+accum'+extkypng)
        shutil.copy(loupng, NIDSOUTMAP+'+pcpn+accum'+extloupng)
        # show maps
        self.gui.addMessage('All tasks completed, popping up viewers.\n\n')
        subprocess.Popen((PNGVIEW, wfopng))
        subprocess.Popen((PNGVIEW, kypng))
        subprocess.Popen((PNGVIEW, loupng))
        subprocess.Popen((CSVVIEW, LDADINPUT+'\\accum_pcpn.csv'))

    def runTemp(self):
        """ make the temperature maps """
        if self.gui.temp[0] == 'Maximum':
            pre = 'max'
        else:
            pre = 'min'
        title = self.gui.temp[1]
        filename = self.gui.temp[2]
        # make shapefile
        n = 1
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makePlot(LDADINPUT+'\\'+pre+'t.csv', 'lon', 'lat', pre+'t.shp')
        wfopng = 's:\\temp_maps\\' + filename
        # make PNG
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makePNG(TEMPLATES+pre+TEMPSUF, title, wfopng)
        # copy to NIDS
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        shutil.copy(wfopng, NIDSOUTMAP+'+temp+'+filename)
        # show map
        self.gui.addMessage('All tasks completed, popping up viewers.\n\n')
        subprocess.Popen((PNGVIEW, wfopng))
        subprocess.Popen((CSVVIEW, LDADINPUT+'\\'+pre+'t.csv'))

    def runSnowd(self):
        """ make the snowd map """
        title = self.gui.snowd[0]
        filename = self.gui.snowd[1]
        # make shapefile
        n = 1
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        if 'Merge' in self.gui.snowd[2]:
            self.joinLsr(CATSNOWD, 'snowd.csv')
            shutil.copy(LDADINPUT+'\\tsnowd.csv', LDADINPUT+'\\snowd.csv')
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
        elif 'Only' in self.gui.snowd[2]:
            self.joinLsr(COPYSNOWD, 'snowd.csv')
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
        self.makePlot(LDADINPUT+'\\snowd.csv', 'lon', 'lat', 'snowd.shp')
        self.makeContour('snowd.shp', 'Snowd', 10, 'snowcontour.shp')
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makeClip('snowcontour.shp', WFO_SHP, 'LMKsnowd_clip.shp')
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makeClip('snowcontour.shp', KY_SHP, 'KYsnowd_clip.shp')
        # make PNGs
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        wfopng = 's:\\snow_maps\\' + filename
        self.makePNG(TEMPLATES+SNOWWFO, title, wfopng)
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        kypng = 's:\\snow_maps\\ky\\' + filename
        self.makePNG(TEMPLATES+SNOWKY, title, kypng)
        # copy to NIDS
        self.gui.addMessage('Step {}: '.format(n))
        shutil.copy(wfopng, NIDSOUTMAP+'+snowd+'+filename)
        shutil.copy(kypng, NIDSOUTMAP+'+snowd+KY+ky'+filename)
        # show maps
        self.gui.addMessage('All tasks completed, popping up viewers.\n')
        subprocess.Popen((PNGVIEW, wfopng))
        subprocess.Popen((PNGVIEW, kypng))
        subprocess.Popen((CSVVIEW, LDADINPUT+'\\snowd.csv'))

    def runWindg(self):
        """ make the wind gust map """
        title = self.gui.windg[0]
        filename = self.gui.windg[2]
        # make shapefile
        n = 1
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        if self.gui.windg[3]:
            self.joinLsr(CATWIND, 'wind_gust.csv')
            shutil.copy(LDADINPUT+'\\twind.csv', LDADINPUT+'\\wind_gust.csv')
            self.gui.addMessage('Step {}: '.format(n))
            n += 1
        self.makePlot(LDADINPUT+'\\wind_gust.csv', 'lon', 'lat', 'windgustpts1.shp')
        # make PNG
        wfopng = 's:\\wind_maps\\' + filename
        self.gui.addMessage('Step {}: '.format(n))
        self.makePNG(TEMPLATES+WINDWFO, title, wfopng)
        # copy to NIDS
        shutil.copy(wfopng, NIDSOUTMAP+'+wind+'+filename)
        # show map
        self.gui.addMessage('All tasks completed, popping up viewers.\n')
        subprocess.Popen((PNGVIEW, wfopng))
        subprocess.Popen((CSVVIEW, LDADINPUT+'\\wind_gust.csv'))

    def runLsr(self):
        """ make the lsr map
            dialog:ezdialog - holds user input
            self.gui.addMessage:method - displays output messages
            self:self - GIS object """
        n = 1
        title = self.gui.lsrg[0]
        ifilename = LDADINPUT + '\\' + self.gui.lsrg[1]
        ofilename = self.gui.lsrg[2]
        # make shapefile
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        self.makePlot(ifilename, 'lon', 'lat', 'lsrpts.shp')
        # make PNG
        self.gui.addMessage('Step {}: '.format(n))
        n += 1
        wfopng = 's:\\LSR maps\\' + ofilename
        kypng = 's:\\LSR maps\\ky\\' + ofilename
        self.makePNG(TEMPLATES+LSRWFO, title, wfopng)
        self.gui.addMessage('Step {}: '.format(n))
        self.makePNG(TEMPLATES+LSRKY, title, kypng)
        # copy to NIDS
        shutil.copy(wfopng, NIDSOUTMAP+'+lsr+'+ofilename)
        shutil.copy(kypng, NIDSOUTMAP+'+lsr+ky+'+ofilename)
        # show map
        self.gui.addMessage('All tasks completed, popping up viewers.\n')
        subprocess.Popen((PNGVIEW, wfopng))
        subprocess.Popen((PNGVIEW, kypng))
        subprocess.Popen((CSVVIEW, ifilename))

def main():
    gui = Gui(Mapper)
    gui.dialog.waitforUser()

if __name__ == '__main__':
    main()
