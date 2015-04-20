import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

class WidgetMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
	self.width = self.engine.gfxMgr.renderWindow.getWidth()
	self.height = self.engine.gfxMgr.renderWindow.getHeight()
	self.overlayManager = ogre.OverlayManager.getSingleton()
	self.panel = self.overlayManager.createOverlayElement("Panel", "myNewPanel")
	self.panel.setMetricsMode(ogre.GMM_PIXELS)#RELATIVE_ASPECT_ADJUSTED)
        self.panel.setPosition(-1, 50)
        self.panel.setDimensions(self.width, self.height)        
        self.panel.setMaterialName("ECSLENT/UI")
        
	self.overlay = self.overlayManager.create("myOverlay")
	self.overlay.add2D(self.panel)
	self.overlay.show()
	self.panel.show()

    def tick(self, dt):
        pass

    def stop(self):
        pass

