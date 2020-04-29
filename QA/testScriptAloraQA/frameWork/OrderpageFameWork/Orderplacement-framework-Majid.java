package com.alora.FrameWorkOrder;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Orderplacement {

	
	public void orderplacement1(WebDriver driver,String StoreName,String StreetName,String APTSuite,String City,
			String State,String zipCode,String datetime,String StreetNameDP,String APTSuiteDP,String CityDP,
			String StateDP,String zipCodeDP,String datetimeDP) {
		
		
		//Step 1: Click on Main button
		String mainXpath = "/html/body/header/div/nav/ul/li[2]/a";
		driver.findElement(By.xpath(mainXpath)).click(); 
		
		//Step 2: Click onOrder Placement
		String orderPlacementXpath = "/html/body/div/div/div/div[2]/div[2]/p[1]/a";
		driver.findElement(By.xpath(orderPlacementXpath)).click();
		
		
		//Step 3: Chose Store from drop down
		String storeXpath = "id_store-store";
		driver.findElement(By.id(storeXpath)).sendKeys(StoreName);
		
		//Step 4: Click on Continue Button   
		String ContXpath = "orderingbutton";
		driver.findElement(By.id(ContXpath)).click();

		//Step 5: Enter Street Name
		String streetXpath = "id_pickup-street";
		driver.findElement(By.id(streetXpath)).sendKeys(StreetName);
		
		//Step 6: Enter APT/Suite
		String APTSuiteXpath = "id_pickup-apt";
		driver.findElement(By.id(APTSuiteXpath)).sendKeys(APTSuite);
		
		//Step 7: Enter City 
		String cityuXpath = "id_pickup-city";
		driver.findElement(By.id(cityuXpath)).sendKeys(City);
		
		//Step 8: Enter State
		String stateXpath = "id_pickup-state";
		driver.findElement(By.id(stateXpath)).sendKeys(State);
		
		//Step 9: Enter ZipCode
		String zipCodeXpath = "id_pickup-zip_code";
		driver.findElement(By.id(zipCodeXpath)).sendKeys(zipCode);
		
		//Step 10: Select Date Time
		String dateTimeXpath = "id_pickup-pickup_at";
		driver.findElement(By.id(dateTimeXpath)).sendKeys(datetime);
		
		//Step 11: Click on Continue Button   
		String Cont1Xpath = "//*[@id=\"orderingbutton\"][2]";
		driver.findElement(By.xpath(Cont1Xpath)).click();	
		
		
		
				//Step 5: Enter Street Name
				String streetDropOffXpath = "id_dropoff-street";
				driver.findElement(By.id(streetDropOffXpath)).sendKeys(StreetNameDP);
				
				//Step 6: Enter APT/Suite
				String APTSuiteDropoffXpath = "id_dropoff-apt";
				driver.findElement(By.id(APTSuiteDropoffXpath)).sendKeys(APTSuiteDP);
				
				//Step 7: Enter City 
				String cityDropOffXpath = "id_dropoff-city";
				driver.findElement(By.id(cityDropOffXpath)).sendKeys(CityDP);
				
				//Step 8: Enter State
				String stateDropOffXpath = "id_dropoff-state";
				driver.findElement(By.id(stateDropOffXpath)).sendKeys(StateDP);
				
				//Step 9: Enter ZipCode
				String zipCodeDropOffXpath = "id_dropoff-zip_code";
				driver.findElement(By.id(zipCodeDropOffXpath)).sendKeys(zipCodeDP);
				
				//Step 10: Select Date Time
				String dateTimeDropOffXpath = "id_dropoff-drop_off_at";
				driver.findElement(By.id(dateTimeDropOffXpath)).sendKeys(datetimeDP);
				
				//Step 11: Click on Continue Button   
				String Cont2Xpath = "//*[@id=\"orderingbutton\"][2]";
				driver.findElement(By.xpath(Cont2Xpath)).click();	
				
		
	}
	
	
	
}
