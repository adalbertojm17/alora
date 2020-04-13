import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class logIn {
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
			loggIn();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	//this script was to test the functionality of logging into an account.
		public void loggIn() {
			try {
				Thread.sleep(2000);
				driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[4]/a")).click();
				Thread.sleep(2000);
				driver.findElement(By.id("id_username")).sendKeys("j.mister12@gmail.com");
				driver.findElement(By.id("id_password")).sendKeys("P@kemon12");
				driver.findElement(By.id("buttonstandard")).click();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
			
		}
		//Always have the main method to initialize the script and open the browser.
		public static void main(String[] args) {
			
			seleniumScript aloraHomepage = new seleniumScript();
			aloraHomepage.invokeBrowser();
		}
}
