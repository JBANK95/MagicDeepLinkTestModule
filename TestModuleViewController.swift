//
//  TestModuleViewController.swift
//  MagicDeepLinkTestModule
//
//  Created by Snehal Shendge on 03/11/22.
//

import ABCoreComponent

class TestModuleViewController:UIViewController, RoutingProtocol {
    static var routerName = "MDTEST_TESTMODULE_ROUTER_1"
    
    static func route(to destination: ABCoreComponent.RoutingDestination) {
        switch destination.pushSection {
        case "pushsectiontestmodule":
            print("**ROUTING TO TestModuleViewController")
           let vc = TestModuleViewController()
           navigateTo(vc)
         // navigateToViewControllerFromHome(TestModuleViewController.init(), asModal: false)
            
        default:
            print("**DEFAULT")
        }
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = UIColor.systemOrange
    }
    
}
