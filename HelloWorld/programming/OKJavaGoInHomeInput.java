import javax.swing.JOptionPane;

import org.opentutorials.iot.DimmingLights;
import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.Security;
public class OKJavaGoInHomeInput {
	//매개변수(parameter) args //arguments 값이 args로 들어감 // 중괄호 안에서는 args가 사용자가 입력한 
	//값이다
	public static void main(String[] args) {
		String id = args[0];
		String bright = args[1];
		//String id = JOptionPane.showInputDialog("Enter a ID");
		//String bright = JOptionPane.showInputDialog("Enter a Bright level");
		
		// Elevator call
		Elevator myElevator = new Elevator(id); //JAVA APT 507호
		myElevator.callForUp(1); //올라갈거니 엘베를 1층으로 보내라
		
		// Security off
		Security mySecurity = new Security(id); //
		mySecurity.off();
		
		// Light on 
		Lighting hallLamp = new Lighting(id+" / Hall Lamp");
		hallLamp.on();
		
		Lighting floorLamp = new Lighting(id+" / floorLamp");
		floorLamp.on();
		
		DimmingLights moodLamp = new DimmingLights(id+" moodLamp");
		moodLamp.setBright(Double.parseDouble(bright));
		moodLamp.on();
		
	}

}
