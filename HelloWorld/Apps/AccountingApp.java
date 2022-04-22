
public class AccountingApp {

	private static double valueOfSupply;
	private static double vatRate;

	public static void main(String[] args) {
		
		valueOfSupply = 10000;
		vatRate = 0.1;
		double expenseRate = 0.3;
		double VAT = getVAT(valueOfSupply, vatRate);
		double Total = valueOfSupply + VAT;
		double expense = getVAT(valueOfSupply, expenseRate);
		double Income = valueOfSupply - expense;
		double Dividend1 = Income * 0.5;
		double Dividend2 = Income * 0.3;
		double Dividend3 = Income * 0.2;


		System.out.println(("Value of supply : " + valueOfSupply));

		System.out.println("VAT : "+ VAT);
		System.out.println("Total : "+ Total);
		
		
		System.out.println("Expense : " + expense);
		System.out.println("Income : " + Income);
		
		System.out.println("Dividend : " + Dividend1);
		System.out.println("Dividend : " + Dividend2);
		System.out.println("Dividend : " + Dividend3);

	}

	private static double getVAT(double valueOfSupply, double vatRate) {
		return valueOfSupply * vatRate;
	}

}
