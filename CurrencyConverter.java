import java.util.Scanner;
public class CurrencyConverter{
	public static void main(String[] args) {
        double[] rates = {1.0, 0.95, 0.80, 7.11, 83.30};
        String[] currencies = {"USD", "EUR", "GBP", "RMB", "INR"};

        Scanner sc = new Scanner(System.in);

        System.out.print("How much money do you want to exchange：");
        double amount = sc.nextDouble();

        System.out.print("Your currency(1=USD,2=EUR,3=GBP,4=RMB,5=INR)：");
        int a  = sc.nextInt() - 1;

        System.out.print("The currency you want(1=USD,2=EUR,3=GBP,4=RMB,5=INR)：");
        int b = sc.nextInt() - 1;

        double result = amount * rates[b] / rates[a];

        System.out.printf("%.2f %s = %.2f %s",amount, currencies[a], result, currencies[b]);
    }

}
