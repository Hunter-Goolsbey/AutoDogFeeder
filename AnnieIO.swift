//This program has been tested on ios16 for iphones 11 - 14
//Build success contingent upon API endpoint replacement at line 38



import UIKit
import Foundation


class ViewController: UIViewController {
    
    @IBOutlet var get_date: UIDatePicker!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        let formatter = DateFormatter()
        formatter.dateFormat = "HH:mm"
        
        let timePicker = get_date
        
        timePicker?.addTarget(self, action: #selector(timePickerChanged(sender:)), for: UIControl.Event.valueChanged)
        
    
    @objc func timePickerChanged(sender: UIDatePicker){
        let formatter = DateFormatter()
        formatter.dateFormat = "HH:mm"
        let myString = formatter.string(from: sender.date)
      
        print(myString)
        
        var semaphore = DispatchSemaphore (value: 0)
        
        let parameters = "{\n\"title\": \"\(myString)\",\n\"description\": \"---\"\n}"
        let postData = parameters.data(using: .utf8)
        
        var request = URLRequest(url: URL(string: "[[API endpoint]]")!,timeoutInterval: Double.infinity)
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        
        request.httpMethod = "POST"
        request.httpBody = postData
        
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data else {
                print(String(describing: error))
                semaphore.signal()
                return
            }
            print(String(data: data, encoding: .utf8)!)
            semaphore.signal()
        }
        
        task.resume()
        semaphore.wait()
    }

}
