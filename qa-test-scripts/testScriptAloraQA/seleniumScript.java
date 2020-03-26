
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class seleniumScript {
	
	WebDriver driver;
	
	public void invokeBrowser() {
		
		try {
			System.setProperty("webdriver.chrome.driver", "C:\\Users\\eddie\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe");
			driver = new ChromeDriver();
			driver.manage().window().maximize();
			driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
			driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);
			driver.get("http://aloradevs.ddns.net");	
			createAccount();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	/*This is the script for making an account*/
	public void createAccount() {
		driver.findElement(By.xpath("/html/body/div/p/a")).click();
		driver.findElement(By.xpath("/html/body/div/p[3]/a")).click();
		driver.findElement(By.id("id_first_name")).sendKeys("Eddie");
		driver.findElement(By.id("id_last_name")).sendKeys("Jacobs");
		driver.findElement(By.id("id_phone")).sendKeys("8567892310");
		driver.findElement(By.id("id_email")).sendKeys("j.mister12@yahoo.com");
		driver.findElement(By.id("id_username")).sendKeys("ejacobs95");
		driver.findElement(By.id("id_password1")).sendKeys("P@kemon12");
		driver.findElement(By.id("id_password2")).sendKeys("P@kemon12");
		driver.findElement(By.xpath("/html/body/div/form/div/button")).click();
	}
	public static void main(String[] args) {
		
		seleniumScript aloraHomepage = new seleniumScript();
		aloraHomepage.invokeBrowser();
	}

}
