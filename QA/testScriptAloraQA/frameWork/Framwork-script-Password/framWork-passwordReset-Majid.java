package com.alora.FrameWorkPassword;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class passwordReset {

	
	public void userPasswordReset(WebDriver driver,String olPassword, String newPasword) {
		
		
		//Step 1: Click on Main button
		String mainXpath = "/html/body/header/div/nav/ul/li[2]/a";
		driver.findElement(By.xpath(mainXpath)).click(); 
		
		
		String accountXpath = "/html/body/div[2]/div/div/div[1]/div[2]/p[1]/a";
		driver.findElement(By.xpath(accountXpath)).click(); 
		
		
		String changePassword = "/html/body/div[2]/div[1]/div/div[2]/button[3]/a";
		driver.findElement(By.xpath(changePassword)).click(); 
		
		String oldPasswordID = "id_old_password";
		driver.findElement(By.id(oldPasswordID)).sendKeys(olPassword);
		
		String newPasswordID = "id_new_password1";
		driver.findElement(By.id(newPasswordID)).sendKeys(newPasword);		
		
		String confirmPasswordID = "id_new_password2";
		driver.findElement(By.id(confirmPasswordID)).sendKeys(newPasword);	
		
		
		String UpdateID = "secondmainbutton";
		driver.findElement(By.id(UpdateID)).click();	
		
		
	}
}
