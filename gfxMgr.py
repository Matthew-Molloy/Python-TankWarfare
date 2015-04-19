import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import platform

class GfxMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
        self.go()
        self.engine.entityMgr.sceneManager = self.sceneManager
        pass

    def tick(self, dt):
        self.root.renderOneFrame()

    def stop(self):
        self.cleanUp()
        pass

    def go(self):
        self.createRoot()
        self.defineResources()
        self.setupRenderSystem()
        self.createRenderWindow()
        self.initializeResourceGroups()
        self.setupScene()
        self.setupInputSystem()
        self.startRenderLoop()
 
    # The Root constructor for the ogre
    def createRoot(self):
        self.root = ogre.Root()
 
    # Here the resources are read from the resources.cfg
    def defineResources(self):
        cf = ogre.ConfigFile()
        cf.load("resources.cfg")
 
        seci = cf.getSectionIterator()
        while seci.hasMoreElements():
            secName = seci.peekNextKey()
            settings = seci.getNext()
 
            for item in settings:
                typeName = item.key
                archName = item.value
                ogre.ResourceGroupManager.getSingleton().addResourceLocation(archName, typeName, secName)
 
    # Create and configure the rendering system (either DirectX or OpenGL) here
    def setupRenderSystem(self):
        if not self.root.restoreConfig() and not self.root.showConfigDialog():
            raise Exception("User canceled the config dialog -> Application.setupRenderSystem()")
 
 
    # Create the render window
    def createRenderWindow(self):
        self.root.initialise(True, "AS5")
 
    # Initialize the resources here (which were read from resources.cfg in defineResources()
    def initializeResourceGroups(self):
        ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
        ogre.ResourceGroupManager.getSingleton().initialiseAllResourceGroups()
 
    # Now, create a scene here. Three things that MUST BE done are sceneManager, camera and
    # viewport initializations
    def setupScene(self):
        self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, "Default SceneManager")
        self.camera = self.sceneManager.createCamera("Camera")
	self.camera.setPosition(ogre.Vector3(0, 50, 500))
        viewPort = self.root.getAutoCreatedWindow().addViewport(self.camera)


        plane = ogre.Plane ((0, 1, 0), 0)
        meshManager = ogre.MeshManager.getSingleton ()
        meshManager.createPlane ('Ground', 'General', plane,
10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        ent = self.sceneManager.createEntity('GroundEntity', 'Ground')
        self.sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
        ent.setMaterialName ("Examples/GrassFloor")
        ent.castShadows = False
        self.sceneManager.setSkyDome (True, "Examples/CloudySky", 5, 8)


    # here setup the input system (OIS is the one preferred with Ogre3D)

    def setupInputSystem(self):
        windowHandle = 0
        renderWindow = self.root.getAutoCreatedWindow()
        windowHandle = renderWindow.getCustomAttributeUnsignedLong("WINDOW")
        paramList = [("WINDOW", str(windowHandle))]
        t = [("x11_mouse_grab", "false"), ("x11_mouse_hide", "false")]
        paramList.extend(t)
        self.inputManager = OIS.createPythonInputSystem(paramList)
 
        # Now InputManager is initialized for use. Keyboard and Mouse objects
        # must still be initialized separately

        self.joystick1 = None
        self.joystick2 = None
        try:
            self.keyboard = self.inputManager.createInputObjectKeyboard(OIS.OISKeyboard, False)
            self.mouse = self.inputManager.createInputObjectMouse(OIS.OISMouse, False)
        except Exception, e:
            raise e

        try:
            self.joystick1 = self.inputManager.createInputObjectJoyStick(OIS.OISJoyStick, True)
        except Exception, e:
            self.joystick1 = None
            print "No JoyStick1"


        try:
            self.joystick2 = self.inputManager.createInputObjectJoyStick(OIS.OISJoyStick, True)
        except Exception, e:
            self.joystick2 = None
            print "No JoyStick2"


 
    def startRenderLoop(self):
        self.root.renderOneFrame
 
    # This is the rendering loop
    def startRenderLoop(self):
        self.root.renderOneFrame()
 
    # In the end, clean everything up (= delete)
    def cleanUp(self):
        self.inputManager.destroyInputObjectKeyboard(self.keyboard)
        self.inputManager.destroyInputObjectMouse(self.mouse)
        OIS.InputManager.destroyInputSystem(self.inputManager)
        self.inputManager = None
 
