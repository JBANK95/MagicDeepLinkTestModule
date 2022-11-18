 public final class MagicDeepLinkTestModule { }

// Add to every module that's part of deep linking wherever the configuration or initialization is done
// this will permit external classes to access underlying bundle resources.
/* public final class MagicDeepLinkTestModuleBundle {
   public static let resourceBundle: Bundle = {
        let myBundle = Bundle(for: MagicDeepLinkTestModuleBundle.self)

        guard let resourceBundleURL = myBundle.url(
            forResource: "MagicDeepLinkTestModuleBundle", withExtension: "bundle")
            else { fatalError("MagicDeepLinkTestModuleBundle.bundle not found!") }

        guard let resourceBundle = Bundle(url: resourceBundleURL)
            else { fatalError("Cannot access MagicDeepLinkTestModuleBundle.bundle!") }

        return resourceBundle
    }()

     public static func getModuleRoutes() -> NSMutableDictionary? {
        let moduleBundle = MagicDeepLinkTestModuleBundle.resourceBundle
        if let plistRouteFile = moduleBundle.path(forResource: "DeepLinkingPushSectionMapping", ofType: "plist") {
            print(NSMutableDictionary(contentsOfFile: plistRouteFile))
            return NSMutableDictionary(contentsOfFile: plistRouteFile)
        }
        
        return nil
    }
}*/
