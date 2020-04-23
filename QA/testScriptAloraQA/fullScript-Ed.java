
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
/**
 * Upon Script Testing for Alora, The test Case Script name(method)
 * will constantly change throughout testing, so all scripting is on one sheet but
 * under method names.
 * @author Eddie Jacobs
 *
 */

public class seleniumScript {
	
	//businssAccountScripts b = new businssAccountScripts();
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
			loginBusinessSide();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	//this script is for placing an order
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
	/*
	 * This Section are for account functionality, underneath are codes for making an account, login, and edit profile
	 */
	//this script was to test the functionality of creating an account on Alora's website
	public void createAccount() {
			try {
				driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[4]/a")).click();
				Thread.sleep(3000);
				driver.findElement(By.xpath("/html/body/div/div/p[2]/a")).click();
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
		//this script was to test the functionality of logging into an account.
	public void logIn() {
			try {
				Thread.sleep(2000);
				driver.findElement(By.xpath("/html/body/div/p/a")).click();
				Thread.sleep(2000);
				driver.findElement(By.id("id_username")).sendKeys("tester");
				driver.findElement(By.id("id_password")).sendKeys("tester");
				driver.findElement(By.id("buttonstandard")).click();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}


		}
		//this script was to test the change password functionality.
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

		//this script was to test the edit profile functionality.
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
	public void logInwithUserName() {
			try {
				Thread.sleep(2000);
				driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[4]/a")).click();
				Thread.sleep(2000);
				driver.findElement(By.id("id_username")).sendKeys("ejacobs95");
				driver.findElement(By.id("id_password")).sendKeys("P@kemon12");
				driver.findElement(By.id("buttonstandard")).click();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		}

	/*
	 * This Section is for working within the business Account (Manager Account)
	 * After Scripts are written, they will be copied into its own class
	 */
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
	//simple script to navigate through Alora's website.
	public void nagivateAlora() {
		try {
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[2]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[3]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[4]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[5]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[6]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[7]/a")).click();
			Thread.sleep(2000);
			driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[1]/a")).click();
			Thread.sleep(2000);
			driver.close();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	//this script is to test logging into an Alora account with an user name.

	//Always have the main method to initialize the script and open the browser.
	public static void main(String[] args) {	
		seleniumScript aloraHomepage = new seleniumScript();
		aloraHomepage.invokeBrowser();
	}

}
