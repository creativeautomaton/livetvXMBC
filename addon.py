import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello LiveTv.sx World!"
line2 = " Soon this will have a list os links." 
 
xbmcgui.Dialog().ok(addonname, line1, line2)
