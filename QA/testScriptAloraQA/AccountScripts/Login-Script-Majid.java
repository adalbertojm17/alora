import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class seleniumTest {

	public static void main(String[] args) {
		
		
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		//step 1: Launch firefox and navigate to URL
		driver.get("http://aloraqa.ddns.net/");
		
		//step 2: Click on Login button
		String login_Xpath = "//*[@id=\"navbar\"]/nav/ul/li[4]/a";
		driver.findElement(By.xpath(login_Xpath)).click();
		
		//Step 3: Enter Username and password
		
		//String userNameXPath = "id_email";
		String userNameXPath = "id_username";
		String userName = "majida5";
		driver.findElement(By.id(userNameXPath)).sendKeys(userName);
		//Thread.sleep(2000);
		String passwordXpath = "id_password";
		String password = "David@1234";
		driver.findElement(By.id(passwordXpath)).sendKeys(password);
		
		
		//Step 4: Click on Login Button
		
		String loginBtn = "buttonstandard";
		driver.findElement(By.id(loginBtn)).click();

		//*[@id="id_username"]

		
	}

}