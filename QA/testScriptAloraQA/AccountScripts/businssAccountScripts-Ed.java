import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class businssAccountScripts {
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
	public void loginBusinessSide() {
		try {
			Thread.sleep(2000);
			jse = (JavascriptExecutor)driver;
			jse.executeScript("scroll(0,1100)");
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div/p/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("id_username")).sendKeys("admin2");
			driver.findElement(By.id("id_password")).sendKeys("P@kemon12");
			driver.findElement(By.id("buttonstandard")).click();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void businessAccountFirstNameEdit() {
		try {
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[7]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[1]/div/div[2]/button[1]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("id_first_name")).sendKeys("Eddie");;
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[2]/form/div/button"));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void businessAccountLastNameEdit() {
		try {
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[7]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[1]/div/div[2]/button[1]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("id_last_name")).sendKeys("Russ");;
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[2]/form/div/button"));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void businessAccountEmailEdit() {
		try {
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[7]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[1]/div/div[2]/button[1]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("id_email")).sendKeys("j@dmai");;
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[2]/form/div/button"));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void businessAccountPhoneEdit() {
		try {
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[7]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[1]/div/div[2]/button[1]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("id_phone")).sendKeys("Eddie");;
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[2]/form/div/button"));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void businessAccountUserNameEdit() {
		try {
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[7]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[1]/div/div[2]/button[1]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.id("id_username")).sendKeys("admin98");;
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/div[2]/div[2]/form/div/button"));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void main(String[] args) {	
		seleniumScript aloraQA = new seleniumScript();
		aloraQA.invokeBrowser();
	}
}
