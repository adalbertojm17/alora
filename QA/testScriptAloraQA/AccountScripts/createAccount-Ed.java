import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class createAccount {
	WebDriver driver;
	JavascriptExecutor jse;
	//this method is setting up the browser you wish to use, and window size
	public void invokeBrowser() {
 		
		try {
			System.setProperty("webdriver.chrome.driver", "C:\\Users\\eddie\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe");
			driver = new ChromeDriver();
			driver.manage().window().maximize();
			driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
			driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);
			driver.get("http://aloraqa.ddns.net");	
			makeAccount();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	//this script was to test the functionality of creating an account on Alora's website
		public void makeAccount() {
			try {
				driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[4]/a")).click();
				Thread.sleep(3000);
				driver.findElement(By.xpath("/html/body/div/p[2]/a")).click();
				Thread.sleep(2000);
				driver.findElement(By.id("id_0-first_name")).sendKeys("Pablo");
				driver.findElement(By.id("id_0-last_name")).sendKeys("Jacobs");
				driver.findElement(By.id("id_0-phone")).sendKeys("+18567892343");
				driver.findElement(By.id("id_0-email")).sendKeys("eddie_jacobs@bloomfield.edu");
				driver.findElement(By.id("id_0-email2")).sendKeys("eddie_jacobs@bloomfield.edu");
				driver.findElement(By.id("id_0-username")).sendKeys("Experiment23");
				driver.findElement(By.id("id_0-password1")).sendKeys("P@kEmon12");
				driver.findElement(By.id("id_0-password2")).sendKeys("P@kEmon12");
				Thread.sleep(3000);
				driver.findElement(By.xpath("/html/body/div/form/button")).click();
				Thread.sleep(2000);
				driver.findElement(By.id("id_1-street")).sendKeys("Siebel");
				driver.findElement(By.id("id_1-apt")).sendKeys("40");
				driver.findElement(By.id("id_1-city")).sendKeys("Bridgeton");
				driver.findElement(By.id("id_1-state")).click();
				Thread.sleep(2000);
				driver.findElement(By.xpath("/html/body/div/form/p[7]/select/option[28]")).click();
				Thread.sleep(2000);
				driver.findElement(By.id("id_1-zip_code")).sendKeys("08302");
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		public static void main(String[] args) {	
			seleniumScript aloraHomepage = new seleniumScript();
			aloraHomepage.invokeBrowser();
		}
}
