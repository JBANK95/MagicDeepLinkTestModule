import ABCoreComponent

// Add to every module that's part of deep linking wherever the configuration or initialization is done
// this will permit external classes to access underlying bundle resources.
// Copy/Paste and change the forResource name to the one defined in podspec
public final class ModuleInitialization: DeepLinkingModuleConformance {
    public static let resourceBundle: Bundle = {
        let myBundle = Bundle(for: ModuleInitialization.self)

        guard let resourceBundleURL = myBundle.url(
            forResource: "MagicDeepLinkTestModuleBundle", withExtension: "bundle")
            else { fatalError("MagicDeepLinkTestModuleBundle.bundle not found!") }

        guard let resourceBundle = Bundle(url: resourceBundleURL)
            else { fatalError("Cannot access MagicDeepLinkTestModuleBundle.bundle!") }

        return resourceBundle
    }()

     public static func getModuleRoutes() -> NSMutableDictionary? {
        let moduleBundle = ModuleInitialization.resourceBundle
        if let plistRouteFile = moduleBundle.path(forResource: "DeepLinkingPushSectionMapping", ofType: "plist") {
            print(NSMutableDictionary(contentsOfFile: plistRouteFile))
            return NSMutableDictionary(contentsOfFile: plistRouteFile)
        }
        
        return nil
    }
    
}
