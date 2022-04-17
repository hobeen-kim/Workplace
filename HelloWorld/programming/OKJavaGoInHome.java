import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.Security;
public class OKJavaGoInHome {

	public static void main(String[] args) {
		String id = "JAVA APT 507";
		
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
		
	}

}
