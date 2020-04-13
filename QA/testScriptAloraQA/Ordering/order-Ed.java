import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class order {
	
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
			driver.get("http://aloradevs.ddns.net");	
			orderUp();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void orderUp() {
		try {
			driver.findElement(By.xpath("/html/body/div/div[2]/div[2]/p[1]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div/form/p/select")).click();
			driver.findElement(By.xpath("/html/body/div/form/p/select/option[3]")).click();
			driver.findElement(By.xpath("/html/body/div/form/button")).click();
			driver.findElement(By.id("id_pickup-street")).sendKeys("Siebe Street");
			driver.findElement(By.id("id_pickup-apt")).sendKeys("40");
			driver.findElement(By.id("id_pickup-city")).sendKeys("Bridgeton");
			Thread.sleep(4000);
			driver.findElement(By.id("id_pickup-state")).click();
			driver.findElement(By.xpath("/html/body/div/form/p[4]/select/option[37]")).click();
			Thread.sleep(2000);
			jse = (JavascriptExecutor)driver;
			jse.executeScript("scroll(0,1100)");
			Thread.sleep(3000);
			driver.findElement(By.id("id_pickup-zip_code")).sendKeys("08302");
			driver.findElement(By.xpath("/html/body/div/form/div/input")).sendKeys("April 15, 2020 5:23");
			driver.findElement(By.xpath("/html/body/div/form/button[2]")).click();
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
