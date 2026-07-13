Executive Business Report
Streamlit link- https://salesforecastingusingprophetxgbsarima.streamlit.app/
Sales Forecasting and Demand Analysis for Retail Inventory Planning
Executive Summary
This report presents the findings of a sales analytics and forecasting study conducted on historical retail sales data to support inventory planning and business decision-making. Historical sales patterns were analyzed to understand demand trends across product categories and geographical regions. A forecasting model was developed to estimate future sales, unusual sales patterns were identified using anomaly detection techniques, and products were grouped into demand segments for inventory planning. The analysis indicates that East region and Office Supplies are expected to generate the highest sales over the next three months. While most demand follows predictable seasonal trends, a few exceptional sales weeks were identified, likely corresponding to promotional events or seasonal shopping periods. The findings provide actionable recommendations to improve inventory allocation, reduce stock shortages, and optimize working capital.

1. Key Findings from Data Analysis and Forecasting
Historical sales analysis revealed a consistent upward trend in overall sales with noticeable seasonal fluctuations. Sales volumes increased significantly during major shopping periods, particularly in the final quarter of each year, indicating strong seasonal demand.
Category-level analysis showed that Technology and Office Supplies consistently generated higher revenue than Furniture. Region-wise analysis indicated that the East and West regions contributed the largest share of overall sales, suggesting that these markets should receive greater operational focus.
Among the forecasting models evaluated, Extreme Gradient Boosting (XGBoost) produced the lowest prediction error and was selected as the final forecasting model because it captured both long-term trends and short-term fluctuations more effectively than the alternative models.
Three-Month Sales Forecast
Segment	Forecasted Sales
East Region	366,798
Office Supplies	353,370
Technology	320,216
West Region	275,058
Furniture	175,822
The forecast suggests that demand is expected to remain strongest in the East region, followed closely by Office Supplies products. Furniture is projected to experience comparatively lower demand during the forecast horizon.
Forecast Confidence 
Although no forecasting model can predict future sales with complete certainty, the XGBoost model demonstrated the best prediction accuracy among all evaluated models. Based on historical performance, the projected sales are expected to remain within approximately ±10–15% of the forecasted values under normal business conditions. Significant external events such as major promotions, economic changes, or supply chain disruptions may lead to deviations outside this range.
________________________________________
2. Top Three Sales Anomalies
The anomaly detection process identified several weeks where sales deviated substantially from the normal trend. The most significant anomalies include:
Approximate Period	Likely Business Explanation
March 2015	Exceptional sales spike, likely caused by a promotional campaign or bulk corporate purchases.
November 2018	High sales activity corresponding to festive shopping and year-end promotional events.
December 2018	Strong holiday season demand resulting in unusually high weekly sales.
The comparison of Isolation Forest and Rolling Z-Score methods showed that while both techniques identified several common anomalies, each also detected unique events. This suggests that combining multiple detection methods provides a more comprehensive understanding of unusual sales behaviour.
________________________________________
3. Product Demand Segmentation
Products were grouped into four demand segments using K-Means clustering based on total sales, sales growth, demand volatility, and average order value.
Demand Segment	Characteristics	Recommended Inventory Strategy
High Volume, Stable Demand	High sales with consistent demand	Maintain higher inventory levels and prioritize replenishment.
Growing Demand	Moderate sales with strong growth	Increase inventory gradually while monitoring demand trends.
High Value, Rapid Growth	High-value products with rapid growth but greater variability	Maintain safety stock and monitor demand frequently to avoid stockouts.
Low Volume, Stable Demand	Lower sales with predictable demand	Maintain lean inventory and replenish only when required.
This segmentation enables differentiated inventory policies instead of applying a uniform stocking strategy across all products.

4. Business Recommendations
Recommendation 1: Prioritize Inventory Allocation for the East Region
The East region is forecasted to generate approximately 366,798 in sales over the next three months, making it the strongest-performing region. Increasing inventory availability and replenishment frequency in this region will help reduce stockouts and improve customer satisfaction.

Recommendation 2: Increase Stock Levels for Office Supplies
Office Supplies is expected to remain the highest-performing product category with forecasted sales of approximately 353,370. Maintaining sufficient inventory for these products will maximize sales opportunities while reducing the risk of lost revenue due to unavailable stock.

Recommendation 3: Adopt Demand-Based Inventory Policies
The clustering analysis demonstrates that different product groups exhibit distinct demand patterns. Applying customized inventory strategies based on demand segments can improve inventory turnover, reduce excess stock, and lower holding costs compared to using a single replenishment policy for all products.

5. Business Risk and Limitation
The forecasting system relies primarily on historical sales data and assumes that future demand patterns will remain similar to those observed in the past. Unexpected events such as new competitors, pricing changes, supply chain disruptions, economic conditions, or large promotional campaigns may significantly influence future sales and reduce forecast accuracy. Therefore, the forecasting model should be updated regularly with the latest sales data to maintain reliable predictions.



![alt text](<Screenshot (105).png>)

![alt text](<Screenshot (106).png>)

![alt text](<Screenshot (108).png>)

![alt text](<Screenshot (109).png>)
