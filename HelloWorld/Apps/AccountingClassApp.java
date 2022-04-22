class Accounting{
	public double valueOfSupply;
	public double vatRate;
	public double expenseRate;

	public void print() {
		System.out.println(("Value of supply : " + valueOfSupply));

		System.out.println("VAT : "+ getVAT());
		System.out.println("Total : "+ getTotal());
		
		
		System.out.println("Expense : " + getExpense());
		System.out.println("Income : " + getincome());
		
		System.out.println("Dividend : " + getDividend1());
		System.out.println("Dividend : " + getDividend2());
		System.out.println("Dividend : " + getDividend3());
	}



	public double getDividend1() {
		return getincome() * 0.5;
	}
	public double getDividend2() {
		return getincome() * 0.3;
	}
	public double getDividend3() {
		return getincome() * 0.2;
	}

	public double getincome() {
		return valueOfSupply - getExpense();
	}

	public double getExpense() {
		return valueOfSupply * expenseRate;
	}

	public double getTotal() {
		return valueOfSupply + getVAT();
	}

	public double getVAT() {

		return valueOfSupply * vatRate;
	}
}

public class AccountingClassApp {


	public static void main(String[] args) {
		

		// instance
		// Accounting class 복제
		Accounting a1 = new Accounting();
		a1.valueOfSupply = 20000.0;
		a1.vatRate = 0.5;
		a1.expenseRate = 0.1;
		
		a1.print();

		
	}





}
