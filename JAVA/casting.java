
public class casting {
	public static void main(String[] args) {
		double a = 1.1;
		double b = 1;
		System.out.println(b); //b는 double형이지만 1(int)로도 설정 가능
		
//		int c = 1.1;
		double d = 1.1; // int -> double 
		int e = (int) 1.1; //1.1 -> (int) 1.1 --> 손실이 일어남
		System.out.println(d);
		
		// 1 to String
		String f = Integer.toString(1);
		System.out.println(f.getClass());

	}
}
