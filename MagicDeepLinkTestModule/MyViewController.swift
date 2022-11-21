
import ABCoreComponent

class MyViewController: UIViewController, RoutingProtocol {
    
    static let routerName = "MAIN_ROUTER"
    static func route(to destination: RoutingDestination) {
        switch destination.pushSection {
        case "developmentpushsection":
            print("**ROUTING TO MYUIVIEWCONTROLLER")
            navigateToViewControllerFromHome(MyViewController.init(), asModal: false)
            
        default:
            print("**DEFAULT")
        }
    }
    var blackSquare: UIView!
     
    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.backgroundColor = UIColor.green
        blackSquare = UIView(frame: CGRect(x: 0.0, y: 0.0, width: 100, height: 100))
        blackSquare.backgroundColor = UIColor.black
        view.addSubview(blackSquare)
        
    }
}
