import ogre.renderer.OGRE as ogre


class WidgetMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
        self.width = self.engine.gfxMgr.camera.getViewport().getActualWidth()
        self.height = self.engine.gfxMgr.camera.getViewport().getActualHeight()
        self.overlayManager = ogre.OverlayManager.getSingleton()
        self.xOffset = 40
        self.yOffset = self.height - 90

        self.panel = self.overlayManager.createOverlayElement("Panel", "myNewPanel")
        self.panel.setMetricsMode(ogre.GMM_PIXELS)  # RELATIVE_ASPECT_ADJUSTED)
        self.panel.setPosition(0, 0)
        self.panel.setDimensions(self.width, self.height)
        self.panel.setMaterialName("ECSLENT/UI")

        self.textArea = self.overlayManager.createOverlayElement("TextArea", "leftText");
        self.panel.addChild(self.textArea)
        self.textArea.setMetricsMode(ogre.GMM_PIXELS)
        self.textArea.setPosition(self.xOffset, (self.yOffset / 2) - 50)
        self.textArea.setDimensions(self.width, self.height)
        self.textArea.setFontName("BlueHighway")
        self.textArea.setCharHeight(self.height / 40)
        self.textArea.setColour((1.0, 1.0, 0.7))

        self.textArea2 = self.overlayManager.createOverlayElement("TextArea", "rightText");
        self.panel.addChild(self.textArea2)
        self.textArea2.setMetricsMode(ogre.GMM_PIXELS)
        self.textArea2.setPosition(self.width - 450, (self.yOffset / 2) - 50)
        self.textArea2.setDimensions(self.width, self.height)
        self.textArea2.setFontName("BlueHighway")
        self.textArea2.setCharHeight(self.height / 40)
        self.textArea2.setColour((1.0, 1.0, 0.7))

        self.text = self.overlayManager.createOverlayElement("TextArea", "Tank 0")
        self.text.setPosition(0.04, 0.89)
        self.text.setDimensions(1, 1)
        self.text.setCaption("Tank 0 Health: 100")
        self.text.setCharHeight(.025)
        self.text.setFontName("StarWars")
        self.text.setColour(( 1, 1, 1 ))
        self.text.setSpaceWidth(.01)
        self.panel.addChild(self.text)

        self.text = self.overlayManager.createOverlayElement("TextArea", "Tank 1")
        self.text.setPosition(0.78, 0.89)
        self.text.setDimensions(1, 1)
        self.text.setCaption("Tank 1 Health: 100")
        self.text.setCharHeight(.025)
        self.text.setFontName("StarWars")
        self.text.setColour(( 1, 1, 1 ))
        self.text.setSpaceWidth(.01)
        self.panel.addChild(self.text)

        self.overlay = self.overlayManager.create("myOverlay")
        self.overlay.add2D(self.panel)
        self.textArea.show()
        self.overlay.show()
        self.panel.hide()


    def tick(self, dt):
        self.width = self.engine.gfxMgr.camera.getViewport().getActualWidth()
        self.height = self.engine.gfxMgr.camera.getViewport().getActualHeight()
        self.panel.setPosition(0, 0)
        self.panel.setDimensions(self.width, self.height)

    def stop(self):
        pass
