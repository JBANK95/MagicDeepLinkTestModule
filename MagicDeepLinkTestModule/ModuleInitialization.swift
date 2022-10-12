


public final class MagicDeepLinkTestModuleBundle {
    public static let resourceBundle: Bundle = {
        let myBundle = Bundle(for: MagicDeepLinkTestModuleBundle.self)

        guard let resourceBundleURL = myBundle.url(
            forResource: "MagicDeepLinkTestModuleBundle", withExtension: "bundle")
            else { fatalError("MagicDeepLinkTestModuleBundle.bundle not found!") }

        guard let resourceBundle = Bundle(url: resourceBundleURL)
            else { fatalError("Cannot access MagicDeepLinkTestModuleBundle.bundle!") }

        return resourceBundle
    }()
    
}