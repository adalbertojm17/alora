import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class editAccount {
	
	
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
			editProfile();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void editProfile() {
		try {
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div/div[1]/div[2]/p[1]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("editbutton")).click();
			driver.findElement(By.id("id_first_name")).clear();
			driver.findElement(By.id("id_first_name")).sendKeys("334");
			driver.findElement(By.id("id_last_name")).clear();
			driver.findElement(By.id("id_last_name")).sendKeys("33");
			driver.findElement(By.id("id_phone")).clear();
			driver.findElement(By.id("id_phone")).sendKeys("8775941319");
			driver.findElement(By.id("id_email")).clear();
			driver.findElement(By.id("id_email")).sendKeys("ejacobs@student.cccnj.edu");
			driver.findElement(By.id("id_username")).clear();
			driver.findElement(By.id("id_username")).sendKeys("experiment626");
			Thread.sleep(2000);
			jse = (JavascriptExecutor)driver;
			jse.executeScript("scroll(0,2000)");
			driver.findElement(By.xpath("/html/body/div[2]/form/div/button")).click();
			
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