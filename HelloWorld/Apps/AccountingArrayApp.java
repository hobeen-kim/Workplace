
public class AccountingArrayApp {

	public static void main(String[] args) {
		
		double valueOfSupply = Double.parseDouble(args[0]);
		double vatRate = 0.1;
		double expenseRate = 0.3;
		double VAT = valueOfSupply * vatRate;
		double Total = valueOfSupply + VAT;
		double expense = valueOfSupply * expenseRate;
		double income = valueOfSupply - expense;
		
		double[] dividendRates = new double[3];
		dividendRates[0] = 0.5;
		dividendRates[1] = 0.3;
		dividendRates[2] = 0.2;
		
		
		double Dividend1 = income * dividendRates[0];
		double Dividend2 = income * dividendRates[1];
		double Dividend3 = income * dividendRates[2];
		
		if(income > 10000.0) {
		Dividend1 = income * 0.5;
		Dividend2 = income * 0.3;
		Dividend3 = income * 0.2;
		} else {
			Dividend1 = income * 1;
			Dividend2 = income * 0;
			Dividend3 = income * 0;
		}

		System.out.println(("Value of supply : " + valueOfSupply));

		System.out.println("VAT : "+ VAT);
		System.out.println("Total : "+ Total);
		
		
		System.out.println("Expense : " + expense);
		System.out.println("Income : " + income);
		
		System.out.println("Dividend : " + Dividend1);
		System.out.println("Dividend : " + Dividend2);
		System.out.println("Dividend : " + Dividend3);

	}

}
