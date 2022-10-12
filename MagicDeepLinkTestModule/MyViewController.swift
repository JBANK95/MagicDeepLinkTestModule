class ViewController: UIViewController {
    
    var blackSquare: UIView!
     
    override func viewDidLoad() {
        super.viewDidLoad()
        
        blackSquare = UIView(frame: CGRect(x: 0.0, y: 0.0, width: 100, height: 100))
        blackSquare.backgroundColor = UIColor.black
        view.addSubview(blackSquare)
        
    }
}