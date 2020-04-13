import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class passwordChange {
	public void changePassword() {
		try {
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div/div[1]/div[2]/p[1]/a")).click();
			Thread.sleep(3000);
			driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/button[3]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("id_old_password")).sendKeys("P@kemon12");
			Thread.sleep(2000);
			driver.findElement(By.id("id_new_password1")).sendKeys("ballisLife12");
			Thread.sleep(2000);
			driver.findElement(By.id("id_new_password2")).sendKeys("ballisLife12");
			driver.findElement(By.xpath("/html/body/form/p/button")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[8]/a")).click();
			
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
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
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void main(String[] args) {	
		seleniumScript aloraHomepage = new seleniumScript();
		aloraHomepage.invokeBrowser();
	}
}
