Pod::Spec.new do |spec|
  spec.name         = 'MagicDeepLinkTestModule'
  spec.version      = '1.0.0'
  spec.summary      = 'Test Module'
  spec.license = { :type => 'Commercial', :text => 'Created and licensed by Albertsons Companies. Copyright Albertsons Companies, LLC. All rights reserved.' }
  spec.homepage     = 'https://github.com/kiransar/ABMagicDeeplink-iOS.git'
  spec.authors      = { 'Jonathan Banks' => 'jbank95@safeway.com' }
  spec.source       = { :git => 'https://github.com/JBANK95/ABMagicDeepLinkTestModule.git', :tag => "#{spec.version}" }
  spec.source_files = 'MagicDeepLinkTestModule/**/*', 'MagicDeepLinkTestModule/.MagicDeeplinkConfig', 'MagicDeepLinkTestModule/.MagicDeeplinkConfig/.startup.sh', 'MagicDeepLinkTestModule/.MagicDeeplinkConfig/.startup.sh', 'MagicDeepLinkTestModule/.MagicDeeplinkConfig/.DeepLinkingCompliance.py'
  spec.swift_version = "5.3"
  spec.platform      =  :ios, "11.0"
  spec.static_framework = true
  spec.dependency 'ABMagicDeeplink', '~> 1.0.6'
  spec.script_phases = [
    { :name => 'Precompile',
      :script => '${PODS_TARGET_SRCROOT}/MagicDeepLinkTestModule/.MagicDeeplinkConfig/.DeepLinkingCompliance.py',
      :execution_position => :before_compile
    }
  ]
  spec.resource_bundles = {'MagicDeepLinkTestModuleBundle' => ['MagicDeepLinkTestModule/DeepLinkingPushSectionMapping.plist'] }

end
