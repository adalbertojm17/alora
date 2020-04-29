package com.alora.changepassword;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class changePassword {

	public static void main(String[] args) throws InterruptedException {
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		driver.manage().window().maximize();
		
		//step 1: Launch firefox and navigate to URL
		driver.get("https://aloradevs.ddns.net/");
		
		
		//Step 2: Login with valid user name
		
		String signInXpath = "/html/body/div/p/a";
		driver.findElement(By.xpath(signInXpath)).click();
		
		String userNameXPath = "id_username";
		
		//UserName  -- Change user name 
		String userName = "majid_masood@bloomfield.edu";
		driver.findElement(By.id(userNameXPath)).sendKeys(userName);
		//Thread.sleep(2000);
		String passwordXpath = "id_password";
		//Password  -- Change password
		String password = "Pass@123";
		driver.findElement(By.id(passwordXpath)).sendKeys(password);
		
		String btnLoginID = "buttonstandard";
		driver.findElement(By.id(btnLoginID)).click();
		
		
		Thread.sleep(3000);
		//step 3: Click on Account button 
		String accountXpath = "/html/body/div/div[1]/div[2]/p[1]/a";
		driver.findElement(By.xpath(accountXpath)).click();
		
		//Step 4: Click on Change Password button
		String changePasswordXapth = "/html/body/div[1]/div/div[2]/button[3]/a";
		driver.findElement(By.xpath(changePasswordXapth)).click();
		
		
		//step 5: Change Old Password
		String oldPasswordID = "id_old_password";
		driver.findElement(By.id(oldPasswordID)).clear();
		//Old Password  -- Change Old Password
		driver.findElement(By.id(oldPasswordID)).sendKeys("Pass@123"); 

		//step 6: Change New Password
		String newPasswordID1 = "id_new_password1";
		driver.findElement(By.id(newPasswordID1)).clear();
		//New Password  -- Change New Password
		//driver.findElement(By.id(newPasswordID1)).sendKeys("Pass@1234"); 
		
		//step 7: Change Confirm Password
		String newPasswordID2 = "id_new_password2";
		driver.findElement(By.id(newPasswordID2)).clear();
		//Confirm Password  -- Change Confirm Password
		//driver.findElement(By.id(newPasswordID2)).sendKeys("Pass@1234"); 
		
		Thread.sleep(5000);
		//Step 8: Click on SAVE button
		String changePassID = "secondmainbutton";
		driver.findElement(By.id(changePassID)).click();
		
		
		
	}
}
