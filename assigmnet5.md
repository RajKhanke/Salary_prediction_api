# Smart Agriculture Management System: CRC Cards

**Assignment 5: Class Collaboration-Responsibility (CRC) Cards**

**Name:** Raj Khanke
**Class:** TY CSAIML A
**Roll No:** 31

---

## 1. CropRecommender

| Class Name      | Responsibilities                                                                                                | Collaborators                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------|
| CropRecommender | - Analyze soil NPK values and pH levels<br>- Process climate and geographical data<br>- Generate crop recommendations based on soil parameters<br>- Calculate crop suitability scores | - SoilAnalyzer<br>- WeatherForecaster<br>- CroppingSeasonPredictor |

---

## 2. FertilizerManager

| Class Name        | Responsibilities                                                                                                | Collaborators                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------|
| FertilizerManager | - Determine nutrient deficiencies based on soil data<br>- Recommend appropriate fertilizers and application rates<br>- Predict fertilizer usage based on crop selection<br>- Schedule optimal fertilization timing | - SoilAnalyzer<br>- CropRecommender<br>- SoilReportAnalyzer |

---

## 3. IrrigationController

| Class Name           | Responsibilities                                                                                                | Collaborators                     |
|----------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------|
| IrrigationController | - Calculate crop water requirements<br>- Develop optimal irrigation schedules<br>- Predict water usage based on crop type and weather<br>- Adjust irrigation plans based on real-time soil moisture data | - WeatherForecaster<br>- PumpController<br>- SoilAnalyzer |

---

## 4. PumpController

| Class Name     | Responsibilities                                                                    | Collaborators                           |
|----------------|-------------------------------------------------------------------------------------|-----------------------------------------|
| PumpController | - Monitor irrigation system status<br>- Predict pump on/off timing based on irrigation needs<br>- Control water flow rates and pressure<br>- Report pump performance metrics | - IrrigationController<br>- SoilAnalyzer<br>- GeofencingManager |

---

## 5. DiseaseDetector

| Class Name      | Responsibilities                                                      | Collaborators                      |
|-----------------|-----------------------------------------------------------------------|------------------------------------|
| DiseaseDetector | - Analyze crop images for disease symptoms<br>- Identify disease type and severity<br>- Recommend treatment options<br>- Track disease progression | - PestManager<br>- WeatherForecaster<br>- FertilizerManager |

---

## 6. PestManager

| Class Name  | Responsibilities                                                                                                | Collaborators                        |
|-------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------|
| PestManager | - Monitor pest population trends<br>- Predict pest outbreaks based on environmental factors<br>- Recommend preventive measures<br>- Calculate risk levels for different pest types | - WeatherForecaster<br>- GeospatialAnalyzer<br>- Pestopedia |

---

## 7. GeospatialAnalyzer

| Class Name         | Responsibilities                                                                                                | Collaborators                        |
|--------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------|
| GeospatialAnalyzer | - Map pest distribution patterns<br>- Analyze spatial relationships between pests and crops<br>- Track pest migration patterns<br>- Generate heat maps of infestation risks | - PestManager<br>- GeofencingManager<br>- WeatherForecaster |

---

## 8. GeofencingManager

| Class Name        | Responsibilities                                                                | Collaborators                         |
|-------------------|---------------------------------------------------------------------------------|---------------------------------------|
| GeofencingManager | - Define farm boundaries using GPS coordinates<br>- Monitor asset movement within farm areas<br>- Generate alerts for unauthorized access<br>- Optimize field zoning for crop rotation | - GeospatialAnalyzer<br>- IrrigationController<br>- CropSwapStrategist |

---

## 9. WeatherForecaster

| Class Name        | Responsibilities                                                                                                | Collaborators                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| WeatherForecaster | - Collect and analyze weather data<br>- Generate short and long-term weather predictions<br>- Calculate climate impact on crops<br>- Issue alerts for extreme weather events | - IrrigationController<br>- CroppingSeasonPredictor<br>- PestManager |

---

## 10. SoilAnalyzer

| Class Name    | Responsibilities                                                                      | Collaborators                             |
|---------------|---------------------------------------------------------------------------------------|-------------------------------------------|
| SoilAnalyzer  | - Process soil test results<br>- Track soil nutrient levels over time<br>- Generate soil health metrics<br>- Identify soil improvement opportunities | - FertilizerManager<br>- CropRecommender<br>- SoilReportAnalyzer |

---

## 11. SoilReportAnalyzer

| Class Name         | Responsibilities                                                                                                | Collaborators                       |
|--------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------|
| SoilReportAnalyzer | - Interpret lab soil test reports<br>- Compare results against optimal ranges<br>- Generate user-friendly soil assessment<br>- Recommend soil amendment strategies | - SoilAnalyzer<br>- FertilizerManager<br>- DashboardGenerator |

---

## 12. Pestopedia

| Class Name | Responsibilities                                                      | Collaborators                       |
|------------|-----------------------------------------------------------------------|-------------------------------------|
| Pestopedia | - Maintain database of pest information<br>- Provide identification guides<br>- Detail pest lifecycles and behaviors<br>- Recommend pest-specific control methods | - PestManager<br>- DiseaseDetector<br>- DashboardGenerator |

---

## 13. SchemeAdvisor

| Class Name    | Responsibilities                                                                           | Collaborators                          |
|---------------|--------------------------------------------------------------------------------------------|----------------------------------------|
| SchemeAdvisor | - Track available government farming schemes<br>- Match farmer profiles with relevant programs<br>- Calculate potential benefits from schemes<br>- Guide application processes | - FarmerProfileManager<br>- LoanAdvisor<br>- CropRecommender |

---

## 14. LoanAdvisor

| Class Name  | Responsibilities                                                                 | Collaborators                         |
|-------------|----------------------------------------------------------------------------------|---------------------------------------|
| LoanAdvisor | - Analyze farm financial data<br>- Recommend suitable loan products<br>- Calculate loan eligibility and repayment plans<br>- Compare terms across different financial institutions | - SchemeAdvisor<br>- MarketAnalyzer<br>- FarmerProfileManager |

---

## 15. CropSwapStrategist

| Class Name         | Responsibilities                                                                                     | Collaborators                       |
|--------------------|------------------------------------------------------------------------------------------------------|-------------------------------------|
| CropSwapStrategist | - Analyze crop rotation benefits<br>- Recommend optimal crop swapping sequences<br>- Calculate financial impact of crop changes<br>- Plan transition timelines between crops | - CropRecommender<br>- MarketPlanner<br>- PricePredictor |

---

## 16. StorageManager

| Class Name     | Responsibilities                                                                 | Collaborators                       |
|----------------|----------------------------------------------------------------------------------|-------------------------------------|
| StorageManager | - Monitor post-harvest storage conditions<br>- Predict optimal storage duration<br>- Recommend storage methods for specific crops<br>- Alert on storage condition anomalies | - WeatherForecaster<br>- MarketAnalyzer<br>- PricePredictor |

---

## 17. MarketAnalyzer

| Class Name    | Responsibilities                                                                        | Collaborators                        |
|---------------|-----------------------------------------------------------------------------------------|--------------------------------------|
| MarketAnalyzer| - Track agricultural market trends<br>- Analyze supply and demand patterns<br>- Compare market prices across locations<br>- Identify premium market opportunities | - PricePredictor<br>- MarketPlanner<br>- StorageManager |

---

## 18. MarketPlanner

| Class Name   | Responsibilities                                                                    | Collaborators                       |
|--------------|-------------------------------------------------------------------------------------|-------------------------------------|
| MarketPlanner| - Generate optimal harvest timing plans<br>- Recommend market selection based on prices<br>- Plan transportation logistics<br>- Optimize sales timing for maximum profit | - MarketAnalyzer<br>- PricePredictor<br>- StorageManager |

---

## 19. PricePredictor

| Class Name     | Responsibilities                                                                    | Collaborators                             |
|----------------|-------------------------------------------------------------------------------------|-------------------------------------------|
| PricePredictor | - Forecast future crop prices<br>- Analyze historical price patterns<br>- Calculate price volatility risks<br>- Predict optimal selling windows | - MarketAnalyzer<br>- WeatherForecaster<br>- CroppingSeasonPredictor |

---

## 20. CroppingSeasonPredictor

| Class Name            | Responsibilities                                                                                                | Collaborators                         |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------|
| CroppingSeasonPredictor | - Analyze climate patterns for planting windows<br>- Determine optimal sowing and harvesting dates<br>- Predict seasonal risks and opportunities<br>- Calculate growing degree days for crops | - WeatherForecaster<br>- CropRecommender<br>- PricePredictor 
