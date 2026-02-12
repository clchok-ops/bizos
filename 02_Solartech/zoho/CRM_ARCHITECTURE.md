================================================================================
ZOHO CRM ARCHITECTURE SCAN - COMPREHENSIVE ANALYSIS REPORT
================================================================================
Generated: 2026-02-12
Modules Scanned: 11
Total Fields Analyzed: 560+
Total Custom Fields in Deals: 176
Total Validation Rules: 4
Total Workflow Rules: 0

================================================================================
SECTION 1: DEALS MODULE (CRITICAL) - COMPREHENSIVE ANALYSIS
================================================================================

1.1 LAYOUTS (4 Total)
================================================================================
1. Direct
   - ID: 5586105000001686970

2. Project
   - ID: 5586105000000091023

3. Trading
   - ID: 5586105000059546206

4. Troubleshoot
   - ID: 5586105000045352227


1.2 VALIDATION RULES (4 Total)
================================================================================
1. Validation Rule 1
   - Layout: Direct (5586105000001686970)

2. Validation Rule 2
   - Layout: Direct (5586105000001686970)

3. Validation Rule 3
   - Layout: Direct (5586105000001686970)

4. Validation Rule 4
   - Layout: Troubleshoot (5586105000045352227)

NOTE: All validation rules have been detected but lack explicit names in the
configuration. These rules enforce data integrity across the Direct and
Troubleshoot layouts.


1.3 STAGE FIELD - PIPELINE STAGES (29 Total)
================================================================================
Deal Stage Field (API Name: Stage)
Data Type: Picklist
Used in Layouts: All 4 deal layouts

All Pipeline Stages:
  1. Qualification
  2. Identify Decision Makers
  3. Needs Analysis
  4. Specifying
  5. Value Proposition
  6. Negotiation/Review
  7. Deal Won
  8. Delivery/Claims
  9. Closed Won
  10. Closed Lost
  11. Closed-Lost to Competition
  12. Delivery
  13. Needs Evaluation
  14. Solution Design
  15. Pre Application
  16. Fulfilment
  17. New
  18. Feedback
  19. Delivered
  20. Onboarding
  21. CAS
  22. ST & NEM
  23. Tender
  24. ST & TNB
  25. Idle
  26. Site Assessment
  27. Variation Order
  28. Reactivate
  29. Retention

ANALYSIS:
- Complex multi-stage pipeline suggesting diverse deal types (solar, water,
  housing developments, etc.)
- Multiple "Closed" variations tracking different outcomes
- Delivery/onboarding stages integrated into main pipeline
- CAS, NEM, ST & TNB stages indicate regulatory/technical submission tracking


1.4 ALL LOOKUP FIELDS (7 Total - Show Module Relationships)
================================================================================
1. Account Name (Account_Name)
   → Links to: Accounts Module
   - Purpose: Parent account relationship

2. Contact Name (Contact_Name)
   → Links to: Contacts Module
   - Purpose: Primary contact for deal

3. Payment Terms (Payment_Terms)
   → Links to: Terms_and_Conditions Module
   - Purpose: Define payment structure

4. Delivery Terms (Delivery_Terms)
   → Links to: Terms_and_Conditions Module
   - Purpose: Define delivery conditions and timelines

5. Housing Development (Housing_Development)
   → Links to: Housing_Developments Module
   - Purpose: Link to development projects

6. Referred by (Referred_by)
   → Links to: Contacts Module
   - Purpose: Track referral source contact

7. Confirmation Terms (Confirmation_Terms)
   → Links to: Terms_and_Conditions Module
   - Purpose: Define confirmation/acceptance terms

KEY INSIGHT: Deals link to Terms_and_Conditions module through THREE separate
fields, indicating distinct business processes:
- Payment Terms (how payment flows)
- Delivery Terms (how delivery occurs)
- Confirmation Terms (how acceptance is confirmed)


1.5 ALL CUSTOM FIELDS IN DEALS (176 Total)
================================================================================
Organized by Category:

A. CORE DEAL IDENTIFICATION (5 fields)
  1. Project Title (textarea) - Full project description
  2. Deal No. (autonumber) - System-generated deal number
  3. Deal Type (picklist) - Development Project, Partners, Project (End), Commercial
  4. Project Type (picklist) - Housing, Commercial, Industrial, Public, Partner, Residential
  5. Reference No. (text) - External reference identifier

B. FINANCIAL TRACKING (12 fields)
  6. Estimated Deal Value (currency) - Deal_Value field
  7. Total Collected Amount (currency) - Running collection total
  8. New TNB Bill (currency) - Post-installation TNB billing
  9. Retention (currency) - Amount held/reserved
  10. Delivered (currency) - Amount delivered/invoiced
  11. Deposit (currency) - Initial deposit collected
  12. Preliminaries (currency) - Initial project costs
  13. Addition (currency) - Change order additions
  14. Omission (currency) - Change order deductions
  15. Original Contract Sum (currency) - Initial contract value
  16. VO Amount (currency) - Variation Order amount
  17. Highest TNB Bill (RM) (currency) - Historical peak billing
  18. Estimated Saving Selco (currency) - Savings estimate for Selco product
  19. Estimated Saving ATAP + BATTERY (currency) - Savings for battery combo
  20. Estimated Saving ATAP (currency) - Savings for ATAP alone

  Formula Fields (3):
  - Adjusted Contract Sum (formula) - Original + Additions - Omissions
  - Collection Pending (formula) - Outstanding collection amount
  - Delivery Pending (formula) - Outstanding delivery amount
  - Discounted Total (formula) - Total after discounts applied

C. DATES & TIMELINES (14 fields)
  23. Lead In Date (date) - When opportunity entered pipeline
  24. Delivery Completion Date (date) - Expected delivery finish
  25. Quote Deadline (date) - When quote expires
  26. Due for Delivery (date) - Delivery_Due_Date
  27. Stage Date (date) - When stage changed
  28. Quote Confirmed Date (date) - When quote was accepted
  29. Quote/Tender Deadline (date) - Quote_Tender_Deadline
  30. 1st Delivery Due (date) - st_Delivery_Due
  31. Due for Collection (date) - When payment is due
  32. Truss and Roof Start Date (date)
  33. Road Access Start Date (date)
  34. Truss and Roof Completion Date (date)
  35. Brick Work Start Date (date)
  36. Road Access Completion Date (date)
  37. Brick Work Completion Date (date)
  38. Electrical Completion Date (date)
  39. Electrical Start Date (date)
  40. CPC Date (date) - CPC_Date (Certificate of Practical Completion)
  41. DLP End Date (date) - Defects Liability Period end
  42. Service Due Date (date) - Next maintenance due
  43. Next Payment Date (date) - Next scheduled payment
  44. Last Delivered Date (date) - Most recent delivery
  45. Last Payment Date (date) - Most recent payment
  46. Next Delivery Date (date) - Next scheduled delivery

  DateTime Fields (4):
  - TNB Submission Upload Time (datetime)
  - Seda Customer Doc Upload Time (datetime)
  - Seda Engineering Doc Upload Time (datetime)
  - NEM Submission Upload Time (datetime)
  - TNB TNC Upload Time (datetime)
  - Next Follow Up Time (datetime)

D. TECHNICAL SPECIFICATIONS - SOLAR/WATER/HEATING (28 fields)

  Solar PV System:
  47. Solar PV (boolean) - Has solar PV system
  48. System Size (kWp & kWac) (picklist) - Estimated_System_Size_kWp
  49. System Size (kWac) (double) - System_Size_kWac
  50. System Size (kWp) (double) - System_Size_kWp
  51. Max kWac (double) - Max_kWac - Maximum AC capacity
  52. Module Pic (picklist) - Solar module type/image
  53. Inverter Type (picklist) - String, Hybrid, Off-grid, etc.
  54. Inverter Pic (picklist) - Inverter model/image
  55. DB Box (picklist) - Disconnect box type
  56. DB Box Close Up (picklist) - Closeup photo

  Roof Configuration:
  57. Roof Type (picklist) - Tiles, Flat Concrete, Flat Metal, Metal Klip-lok, etc.
  58. Roof Angle (Degree) (integer) - Installation angle in degrees
  59. Roof Load Evaluation (picklist) - Able to Support, Need Reinforcement, Unable, N/A
  60. Roof Plan (picklist) - All Drawing and Report
  61. Draft Roof Plan (picklist) - Draft_Roof_Plan
  62. Single Line Drawing (picklist) - Electrical diagram
  63. Site Plan (boolean) - Has site plan been provided
  64. Site Condition (picklist) - Condition assessment

  Water/Heating Systems:
  65. Centralized Heater (boolean) - Has centralized heater
  66. Storage Heater (boolean) - Has storage heater
  67. Solar Heater (boolean) - Has solar thermal heater
  68. Solar Heater PV (boolean) - Has solar heater + PV combo
  69. Heat Pump (implied) - From Heater_Type picklist
  70. Heater Type (picklist) - Solar, Solar PV, Storage, Heat Pump, Hybrid
  71. POE Water Filter (boolean) - Point of Entry filter
  72. POU Water Filter (boolean) - Point of Use filter
  73. Water Quality Concerns (picklist) - List of concerns
  74. Dynamic Pressure (bar) (double) - Water system pressure
  75. Consumption (kWh) (double) - Annual consumption estimate

E. ELECTRICAL/TECHNICAL SURVEY (12 fields)
  76. Voltage Type (picklist) - Single Phase, Three Phase
  77. Supply Outlet Size (picklist) - 1/2", 3/4", 1", 1.5", 2"
  78. Usage Type (Grid_System) (picklist) - Grid-tied vs off-grid
  79. Voltage Red Before Install (double) - Pre-installation voltage reading
  80. Voltage Yellow Before Install (double)
  81. Voltage Blue Before Install (double)
  82. Voltage Red After Install (double) - Post-installation verification
  83. Voltage Yellow After Install (double)
  84. Voltage Blue After Install (double)
  85. CT Ratio (double) - Current transformer ratio
  86. Fuse Rating (double) - Electrical fuse specification
  87. TNB Owner (text) - TNB account holder name
  88. TNB Submit (picklist) - TNB_Submit status
  89. TNB T&C (picklist) - TNB_T_C
  90. TNB Contract (picklist) - TNB_Contract type
  91. TnB Tariff Category (picklist) - B, C1, C2, C3, C4, D, E1, E2, E3

F. REGULATORY & COMPLIANCE (13 fields)
  92. NEM Submission (picklist) - NEM: Submitted, Query, Pass, Pending, Ready
  93. NEM_Submission status tracking
  94. Applicant Info (picklist) - Applicant_Info document status
  95. Quite Rent/S&P/Geran/Tenancy Agreement (picklist) - Assessment_Residential_or_Quit_Rent
  96. PVsyst Simulation Report (picklist) - PVsyst_Simulation_Report status
  97. All Drawing and Report (picklist) - Roof_Plan all documents
  98. 3-Month TnB Bill Available (picklist) - With_Historic_Usage flag
  99. Latest 3 Months TNB Bill (boolean) - Months_TNB_Bill_Upload
  100. Tech Specs Submitted (boolean) - Technical specifications flag
  101. Detail Drawings Submitted (boolean) - Engineering drawings flag
  102. Specified (boolean) - Specified status
  103. Load Profile Form (picklist) - Load profile documentation
  104. CAS Study (picklist) - CAS_Study - Grid impact study
  105. RJO Form (picklist) - RJO_Form - Regulatory form
  106. ST and TNB Selco Information Form (picklist) - ST and TNB info form

G. RISK & ASSESSMENT (7 fields)
  107. Risk Score (integer) - Numerical risk assessment (0-100 scale implied)
  108. Risk Level (picklist) - Low, Medium, High
  109. Site Condition (picklist) - Site assessment status
  110. Roof Load Evaluation (picklist) - Structural assessment
  111. Water Quality Concerns (picklist) - Multi-select list of concerns
  112. Defect Reported (picklist) - Multi-select defects found
  113. Last Stage Captured When Idle (text) - Idle stage history tracking

H. PAYMENT & COLLECTION (14 fields)
  114. Payment Terms (lookup) - Links to T&C module
  115. Payment Method (picklist) - Cash, 12/24/36/48/60 Month Instalment
  116. Deposit (%) (percent) - Deposit percentage
  117. Retention (%) (percent) - Retention percentage
  118. Deposit1 (currency) - Dollar amount of deposit
  119. Fully Paid (boolean) - Payment complete flag
  120. Fully Delivered (boolean) - Delivery complete flag
  121. Collection Pending (formula) - Outstanding amount
  122. Due for Collection (date) - Collection due date
  123. Next Payment Date (date) - Next scheduled payment
  124. Last Payment Date (date) - Most recent payment
  125. Last Delivered Amount (currency) - Amount in last delivery
  126. Total Collected Amount (currency) - Running total collected
  127. Update TnC (picklist) - When T&C needs updating

I. DELIVERY & LOGISTICS (9 fields)
  128. Delivery Terms (lookup) - Links to T&C module
  129. Delivery Completion Date (date)
  130. Due for Delivery (date)
  131. Delivery Due Date (date)
  132. Delivery Pending (formula)
  133. Delivery Updates (textarea) - Delivery_and_Collection_Summary
  134. Next Delivery Date (date)
  135. Last Delivered Date (date)
  136. Fully Delivered (boolean)
  137. Last Delivered Amount (currency)

J. VARIATION ORDERS (VO) (4 fields)
  138. VO Approval (picklist) - VO approval status
  139. VO Reason (picklist) - Reason for variation order
  140. VO Amount (currency) - Amount of variation order
  141. Addition (currency) - Addition amount
  142. Omission (currency) - Omission amount

K. DEFECTS & WARRANTY (3 fields)
  143. Defect Reported (picklist) - Multi-select defect types
  144. Defects Liability (Months) (integer) - Defects liability period in months
  145. DLP End Date (date) - When defects liability ends

L. QUOTES & DOCUMENTS (4 fields)
  146. Confirmed Quote (text) - Quote_No field
  147. Quote Deadline (date) - When quote expires
  148. Quote Confirmation Date (date) - When quote accepted
  149. Quote/Tender Deadline (date) - Tender deadline

M. WORKPLAN & MILESTONES (1 field + subform)
  150. Workplan Template (boolean) - Has workplan template been used
  151. Items Needed (subform) - Solution_Proposal_Draft - Line items in deal

N. GEOLOCATION (2 fields)
  152. Latitude (double) - GPS latitude
  153. Longitude (double) - GPS longitude

O. DOCUMENTS/FILES (3 fields)
  154. Workdrive Folder ID (text) - zohoworkdriveforcrm__Workdrive_Folder_ID
  155. Workdrive Folder URL (website) - zohoworkdriveforcrm__Workdrive_Folder_URL
  156. Import Update (boolean) - Data sync flag

P. NPS & FEEDBACK (2 fields)
  157. NPS (integer) - Net Promoter Score (0-10 scale)
  158. Tell Us Why (textarea) - Feedback on NPS

Q. FOLLOW-UP & ACTIONS (3 fields)
  159. Next Follow Up Time (datetime) - Next scheduled action
  160. Follow Up Action (text) - Description of follow-up
  161. Task Assigned (boolean) - Has task been assigned

R. SPECIAL OFFERS/PROGRAMS (4 fields)
  162. Promo Code (picklist) - Promotional code applied
  163. Special Request (picklist) - Special request type
  164. Special Process/Discount/Free (picklist) - Charity, Staff Gift, Relationship Sales, etc.
  165. Community Project (picklist) - Eco Ardence, Eco Sanctuary community flag

S. ONLINE SERVICE REQUESTS (1 field)
  166. Service Requested Online (textarea) - Service_Requested_Online

T. ROI & SAVINGS CALCULATIONS (6 fields)
  167. Estimated Saving Selco (currency) - Annual savings estimate
  168. ROI Selco (text) - Return on investment (text field - likely percentage)
  169. Estimated Saving ATAP + BATTERY (currency) - ATAP + battery savings
  170. ROI ATAP + Battery (text) - ATAP + battery ROI
  171. Estimated Saving ATAP (currency) - ATAP only savings
  172. ROI ATAP (text) - ATAP only ROI
  173. System Marginal Price (SMP) (currency) - Electricity pricing

U. BILLING INFORMATION (3 fields)
  174. Highest TNB Bill (RM) (currency) - Highest historical bill
  175. New TNB Bill (currency) - Post-installation bill
  176. Consumption (kWh) (double) - Energy consumption

ADDITIONAL FIELDS:
  177. Confirmation Terms (lookup) - Links to T&C module
  178. Housing Development (lookup) - Links to Housing_Developments module
  179. Referred by (lookup) - Links to Contacts module (referral source)
  180. Account Name (lookup) - Links to Accounts module
  181. Contact Name (lookup) - Links to Contacts module
  182. Relevant Persons (multiselectlookup) - Multiple contacts for deal
  183. Needs (multiselectpicklist) - Multi-select needs assessment
  184. Record No. (integer) - Sequential record number
  185. O&M Cost (currency) - Operations & Maintenance annual cost
  186. Daytime Use (double) - Daytime energy usage percentage
  187. Battery Size (kWh) (double) - Battery capacity if applicable
  188. Forecast Automatic Fuel Adjustment (AFA) (currency) - AFA charges forecast
  189. Defects Liability (Months) (integer) - DLP period
  190. Date of T&C (date) - When T&C became effective
  191. Contract Installer (picklist) - Assigned installer
  192. PO/AI/EI No. (text) - Purchase order / Approval / Estimate number
  193. PO/LA No. (text) - PO / LA number
  194. B2B (boolean) - Business to Business flag
  195. B2C (boolean) - Business to Consumer flag
  196. Storage Cleaning (boolean) - Has storage cleaning been ordered
  197. Defect Reported (picklist) - Multi-select defect report
  198. Promo Code (picklist) - Promotion applied
  199. Account ID for mapping (text) - Account_ID_for_mapping
  200. Raise for Insurance Task (boolean) - Raise_for_Issuance_Task
  201. Record No. (integer) - Tracking number
  202. Update Pipeline (boolean) - Pipeline update flag
  203. Subtotal (formula) - Line items subtotal
  204. Grand Total (formula) - Final total

1.6 BLUEPRINT DETAILS
================================================================================
No blueprint process is currently configured in the Deals module.
The module uses traditional validation rules and workflow rules instead of
a formal blueprint/approval workflow.

RECOMMENDATION: Consider implementing a Blueprint workflow to enforce:
- Sequence of stage transitions
- Required field completion before advancing stages
- Approval gates at key stages (e.g., before "Deal Won")


================================================================================
SECTION 2: QUOTES MODULE - DETAILED ANALYSIS
================================================================================

2.1 MODULE OVERVIEW
================================================================================
Total Fields: 74
Total Lookup Fields: 7
Total Custom Fields: 38
Total Related Lists: 17
Related to: Deals (parent), Contacts, Accounts, Products, Invoices, Sales Orders

2.2 ALL LOOKUP FIELDS (Relationships)
================================================================================
1. Deal Name (Deal_Name)
   → Deals Module
   - Relationship: Many Quotes to One Deal
   - Purpose: Links quote to parent deal

2. Contact Name (Contact_Name)
   → Contacts Module
   - Relationship: Many Quotes to One Contact
   - Purpose: Quote recipient

3. Account Name (Account_Name)
   → Accounts Module
   - Relationship: Many Quotes to One Account
   - Purpose: Customer account

4. PV ROI Table (PV_ROI_Table)
   → PV_ROI_Table Module
   - Relationship: Many Quotes to One ROI Table
   - Purpose: Links ROI calculations

5. Payment Terms (Payment_Terms)
   → Terms_and_Conditions Module
   - Relationship: Many Quotes to One T&C
   - Purpose: Defines payment structure

6. Delivery Terms (Delivery_Terms)
   → Terms_and_Conditions Module
   - Relationship: Many Quotes to One T&C
   - Purpose: Defines delivery conditions

7. Confirmation Terms (Confirmation_Terms)
   → Terms_and_Conditions Module
   - Relationship: Many Quotes to One T&C
   - Purpose: Defines acceptance terms

2.3 ALL CUSTOM FIELDS IN QUOTES (38 Total)
================================================================================
1. Quote No. (autonumber) - System-generated quote number
2. Deal Type (picklist) - Quote type categorization
3. Quotation Date (date) - When quote was created
4. Quote Confirmation Date (date) - When customer accepted
5. Lock (boolean) - Quote is locked from editing
6. Revision No. (integer) - Version number of quote
7. Solar PV (boolean) - Has solar PV component
8. PV ROI Table (lookup) - Links to ROI calculation table
9. Payment Terms (lookup) - Payment structure from T&C
10. Delivery Terms (lookup) - Delivery terms from T&C
11. To Revise (boolean) - Revise flag - needs updating
12. PO/LA Reference (text) - Purchase order reference
13. Reference No. (text) - Internal reference
14. Project Code (text) - Project identifier
15. Total Discount Amount (currency) - Total discounts applied
16. Total Before Discount Amount (currency) - Subtotal before discounts
17. Contract Type (textarea) - Contract type description
18. Promo Code (picklist) - Promotion code applied
19. Defect Liability Period (Months) (integer) - Warranty period
20. Close Lost (boolean) - Quote was closed/lost flag
21. Delivery Date (date) - Scheduled delivery date
22. Zoho Inventory (boolean) - Synced with Zoho Inventory
23. VO (boolean) - Has variation orders
24. Omission/Addition (picklist) - VO type tracking
25. Fully Delivered (boolean) - All items delivered
26. Fully Paid (boolean) - Quote fully paid
27. 12 IPP 3.5% (formula) - 12-month installment with 3.5% interest
28. 24 IPP 5% (formula) - 24-month installment with 5% interest
29. 36 IPP 6% (formula) - 36-month installment with 6% interest
30. 48 IPP 7% (formula) - 48-month installment with 7% interest
31. 60 IPP 10% (formula) - 60-month installment with 10% interest
32. Confirmation Terms (lookup) - Confirmation T&C
33. Revised (boolean) - Quote has been revised
34. Payment Method (picklist) - Payment method type
35. To Deliver (boolean) - Awaiting delivery flag
36. Deposit (RM) (currency) - Deposit in RM currency
37. Retention (RM) (currency) - Retention in RM currency
38. Special Process/Discount/Free (picklist) - Special pricing type

2.4 RELATED LISTS - WHAT LINKS TO QUOTES (17 Total)
================================================================================
1. Quote_Stage_History - Track stage changes
2. Notes - Attached notes/comments
3. SalesOrders - Sales orders created from quote
4. Quote_Name1 - Invoices generated from quote
5. Activities_Chronological_View - Activity timeline
6. Calls - Phone call records
7. Events - Calendar events
8. Tasks - To-do items
9. Tasks_History - Historical task records
10. Events_History - Historical events
11. Calls_History - Historical calls
12. Activities_Chronological_View_History - Activity history
13. Emails - Email records
14. Locking_Information__s - Document locking info
15. PV_ROI_Table - ROI calculations
16. ZohoSign_Documents - E-signature documents
17. Product9 (Products_X_Quotes) - Line items/products

KEY INSIGHT: Quotes form the bridge between Deals and Orders:
Deals → Quotes → Sales Orders → Invoices → Delivery Orders


================================================================================
SECTION 3: TERMS_AND_CONDITIONS MODULE (CustomModule6)
================================================================================

3.1 MODULE OVERVIEW
================================================================================
Total Fields: 23
Total Custom Fields: 11
Total Related Lists: 24
Module Type: Custom Module 6
Purpose: Central management of payment, delivery, and confirmation terms

3.2 ALL FIELDS WITH DATA TYPES
================================================================================
STANDARD FIELDS (System):
1. Record Status (Record_Status__s) : picklist
2. Terms and Condition Name (Name) : text
3. Terms and Condition Owner (Owner) : ownerlookup
4. Created Time (Created_Time) : datetime
5. Modified Time (Modified_Time) : datetime
6. Last Activity Time (Last_Activity_Time) : datetime
7. Tag (Tag) : text
8. Unsubscribed Mode (Unsubscribed_Mode) : picklist
9. Unsubscribed Time (Unsubscribed_Time) : datetime
10. Record Id (id) : bigint
11. Terms and Condition Image (Record_Image) : profileimage
12. Locked (Locked__s) : boolean

CUSTOM FIELDS:
13. T&C of Delivery Term (T_C_of_Delivery_Term) : textarea
    - Stores delivery term conditions

14. T&C of Payment Term (T_C_of_Payment_Term) : textarea
    - Stores payment term conditions

15. Category (Category) : picklist
    - Values: Payment Terms, Delivery Terms, Confirmation Terms
    - Categorizes the T&C record type

16. Retention (Reserved) : percent
    - Retention percentage held from payments

17. Deposit (Deposit) : percent
    - Deposit percentage required upfront

18. Payment Term (Payment_Term) : picklist
    - Values: Cash on Delivery, Cash before Delivery, Cash on Installation,
             Net 30, Net 45, Net 60, Net 90 on Delivery
    - Defines payment schedule

19. Usage Type (Usage_Type) : picklist
    - Values: B2B, B2C, B2B and B2C
    - Defines whether term applies to business or consumer

20. Days Due from Delivery (Days_Due_from_Delivery) : integer
    - Number of days after delivery for payment due

21. Quote Term Name (Quote_Name) : text
    - Reference name for quotes using this T&C

22. Invoice Term Name (Invoice_Term_Name) : text
    - Reference name for invoices using this T&C

23. Active (Active) : picklist
    - Values: Yes, No
    - Whether T&C is currently active/available

3.3 ALL 24 RELATED LISTS - WHAT CONNECTS TO T&C
================================================================================
ACTIVITY & TRACKING (10 lists):
1. Notes - Attached notes
2. Attachments - Supporting documents
3. Emails - Email communications
4. Tasks - To-do items
5. Events - Calendar events
6. Calls - Phone calls
7. Tasks_History - Historical tasks
8. Events_History - Historical events
9. Calls_History - Historical calls
10. Activities_Chronological_View - Activity timeline
11. Activities_Chronological_View_History - Activity history

RECORD LINKING (4 lists):
12. Entity_Cadences_CustomModule6 - Cadence automations
13. Deals - Direct deal relationships
14. Related_Deals - Related deal records
15. Confirmed_Deals - Deals confirmed with these terms
16. Locking_Information__s - Document locking info

PARENT DOCUMENTS (5 lists):
17. Payment_Terms1 - Quotes using as payment terms
18. Delivery_Terms1 - Quotes using as delivery terms
19. Quote_for_Confirmation - Quotes using as confirmation terms
20. Sales_Order - Sales orders linked
21. Sales_Orders - Multiple sales orders
22. Account - Parent accounts
23. CheckLists - Checklists associated

SYSTEM (1 list):
24. Zoho_Survey - Associated surveys

KEY INSIGHT: T&C module is highly connected with 8 direct module links:
- Deals (3 relationships: Payment, Delivery, Confirmation)
- Quotes (3 relationships: Payment, Delivery, Confirmation)
- Sales_Orders (2 relationships)
- Accounts (1 relationship)

This makes T&C a critical master data module for defining business processes.


================================================================================
SECTION 4: DELIVERY_ORDERS MODULE (CustomModule1)
================================================================================

4.1 MODULE OVERVIEW
================================================================================
Total Fields: 29
Total Lookup Fields: 5
Total Custom Fields: 14
Total Related Lists: 6
Module Type: Custom Module 1
Purpose: Track physical delivery of goods/services

4.2 ALL FIELDS WITH DATA TYPES
================================================================================
STANDARD SYSTEM FIELDS:
1. Record Status (Record_Status__s) : picklist
2. Subject (Name) : text - Delivery order description
3. Delivery Order Owner (Owner) : ownerlookup - Record owner
4. Created By (Created_By) : ownerlookup
5. Modified By (Modified_By) : ownerlookup
6. Created Time (Created_Time) : datetime
7. Modified Time (Modified_Time) : datetime
8. Last Activity Time (Last_Activity_Time) : datetime
9. Layout (Layout) : layout - Associated layout
10. Tag (Tag) : text - Tags for organization
11. Unsubscribed Mode (Unsubscribed_Mode) : picklist
12. Unsubscribed Time (Unsubscribed_Time) : datetime
13. Record Id (id) : bigint

CUSTOM CORE FIELDS:
14. Delivery Order No. (Delivery_Order_No) : autonumber
    - System-generated delivery order number

15. Status (Status) : picklist
    - Delivery order status tracking

16. Delivery Order Date (Delivery_Order_Date) : date
    - When delivery order was created

LOOKUP FIELDS (5 - Show Relationships):
17. Contact Name (Contact_Name) : lookup → Contacts
    - Delivery recipient contact

18. Deal Name (Deal_Name) : lookup → Deals
    - Parent deal for delivery

19. Sales Order (Sales_Order) : lookup → Sales_Orders
    - Original sales order

20. Invoice Name (Invoice_Name) : lookup → Invoices
    - Associated invoice

21. Account Name (Account_Name) : lookup → Accounts
    - Customer account

SHIPPING/LOCATION FIELDS (6):
22. Shipping Street (Shipping_Street) : text
    - Street address for delivery

23. Shipping State (Shipping_State) : text
    - State/province for delivery

24. Shipping City (Shipping_City) : text
    - City for delivery

25. Shipping Country (Shipping_Country) : text
    - Country for delivery

26. Shipping Code (Shipping_Code) : text
    - Postal code for delivery

27. Shipping Country (Picklist) (Shipping_Country_Picklist) : picklist
    - Country from standard picklist

LINE ITEMS:
28. Delivery Order Item (Delivery_Order_Item) : subform
    - Individual items being delivered

SYSTEM:
29. Locked (Locked__s) : boolean
    - Record is locked

4.3 RELATED LISTS - CONNECTIONS (6 Total)
================================================================================
1. Notes - Associated notes
2. Emails - Email communications
3. Entity_Cadences_CustomModule1 - Cadence automations
4. CheckLists - Associated checklists
5. Locking_Information__s - Locking details
6. Zoho_Survey - Associated surveys

ANALYSIS: Delivery_Orders is a simple, focused module with:
- Minimal related lists (only activity & system records)
- Heavy reliance on lookups for relationships
- Single address block for shipping
- Subform for line items


================================================================================
SECTION 5: COMPREHENSIVE CROSS-MODULE RELATIONSHIP MAP
================================================================================

5.1 PRIMARY FLOW: DEAL → QUOTE → ORDER → DELIVERY → INVOICE
================================================================================

STEP 1: DEAL CREATION
  Module: Deals
  Key Fields:
    - Account Name (lookup) → Accounts
    - Contact Name (lookup) → Contacts
    - Payment Terms (lookup) → Terms_and_Conditions
    - Delivery Terms (lookup) → Terms_and_Conditions
    - Confirmation Terms (lookup) → Terms_and_Conditions
    - Housing Development (lookup) → Housing_Developments
    - Referred by (lookup) → Contacts

STEP 2: QUOTE GENERATION
  Module: Quotes
  Key Lookups:
    - Deal Name → Deals (many quotes per deal possible)
    - Account Name → Accounts (from deal)
    - Contact Name → Contacts (from deal)
    - Payment Terms → Terms_and_Conditions (can override deal terms)
    - Delivery Terms → Terms_and_Conditions
    - Confirmation Terms → Terms_and_Conditions
    - PV ROI Table → PV_ROI_Table (for solar deals)

STEP 3: SALES ORDER
  Module: Sales_Orders
  Relationship: Created from Quotes (via related list)
  Links to:
    - Deal (implied from quote)
    - Products (via line items)
    - Terms_and_Conditions (payment/delivery)

STEP 4: INVOICE
  Module: Invoices
  Relationship: Created from Sales_Orders (via related list)
  Links to:
    - Deal (implied)
    - Terms_and_Conditions (payment/delivery terms)

STEP 5: DELIVERY
  Module: Delivery_Orders
  Key Lookups:
    - Deal Name → Deals
    - Contact Name → Contacts
    - Account Name → Accounts
    - Sales Order → Sales_Orders
    - Invoice Name → Invoices
  Shipping Info: Complete address captured

STEP 6: CLOSURE
  Back to Deal to mark:
    - Fully Delivered (boolean)
    - Fully Paid (boolean)
    - Delivery Completion Date (date)
    - Last Delivered Date (date)
    - Total Collected Amount (currency)

5.2 TERMS & CONDITIONS AS MASTER DATA
================================================================================

T&C Module Role:
- Central repository for business rules
- Reusable across multiple deals, quotes, and orders
- Three T&C types via Category picklist:
  1. Payment Terms - Cash, Installment, Net 30/45/60/90
  2. Delivery Terms - Conditions for physical delivery
  3. Confirmation Terms - Acceptance/approval conditions

Three-Way Relationship from Deals/Quotes:
  1. Payment_Terms field
  2. Delivery_Terms field
  3. Confirmation_Terms field

Related Lists from T&C:
  - Deals: Links to all deals using these terms
  - Related_Deals: Deals with related terms
  - Confirmed_Deals: Deals confirmed with these terms
  - Payment_Terms1: Quotes using as payment terms
  - Delivery_Terms1: Quotes using as delivery terms
  - Quote_for_Confirmation: Quotes using as confirmation terms
  - Sales_Order / Sales_Orders: Orders using terms
  - Account: Associated account for B2B contracts

5.3 HOUSING DEVELOPMENTS SPECIAL RELATIONSHIP
================================================================================

Deals can link to Housing_Developments via Housing_Development lookup field.

This suggests:
- Developments are master projects
- Deals are sub-projects within developments
- Multiple deals per development (e.g., solar installations across a project)
- Development-level metrics can aggregate deal data

5.4 PRODUCTS INTEGRATION
================================================================================

Products appear in:
- Quote line items (via Products_X_Quotes related list)
- Sales Order line items (via Products_X_Sales_Orders)
- Delivery Order line items (via Delivery_Order_Item subform)

This allows:
- Catalog management in Products module
- Variant selection at quote time
- Quantity changes through order → delivery flow

5.5 CONTACTS & ACCOUNTS HIERARCHY
================================================================================

Accounts (parent organizations):
  ↓
Contacts (individuals at accounts)
  ↓
Deals (opportunities with account/contact)
  ↓
Quotes (quotes to contact at account)

All modules reference both, allowing:
- Multi-contact tracking per account
- Contact-level email/call history
- Account-level analytics

5.6 SPECIAL MODULES

PV_ROI_Table:
- Links to Quotes via lookup
- Likely contains solar ROI calculations
- Used to justify system sizing

Housing_Developments:
- Appears as lookup option in Deals
- Used for project-based tracking
- Allows aggregation of related deals

5.7 COMPLETE RELATIONSHIP MATRIX
================================================================================

Deals connects to:
  ✓ Accounts (lookup)
  ✓ Contacts (lookup × 2: Contact_Name, Referred_by)
  ✓ Terms_and_Conditions (lookup × 3: Payment, Delivery, Confirmation)
  ✓ Housing_Developments (lookup)
  ✓ Quotes (via related list)
  ✓ Sales_Orders (via quotes)
  ✓ Invoices (via sales orders)
  ✓ Delivery_Orders (lookup field Deal_Name)

Quotes connects to:
  ✓ Deals (lookup)
  ✓ Accounts (lookup)
  ✓ Contacts (lookup)
  ✓ Terms_and_Conditions (lookup × 3: Payment, Delivery, Confirmation)
  ✓ PV_ROI_Table (lookup)
  ✓ Products (via line items)
  ✓ Sales_Orders (via related list)
  ✓ Invoices (via related list)

Terms_and_Conditions connects to:
  ✓ Deals (via lookup × 3, via related lists)
  ✓ Quotes (via lookup × 3, via related lists)
  ✓ Sales_Orders (via related lists × 2)
  ✓ Accounts (via related list)

Delivery_Orders connects to:
  ✓ Deals (lookup)
  ✓ Contacts (lookup)
  ✓ Accounts (lookup)
  ✓ Sales_Orders (lookup)
  ✓ Invoices (lookup)


================================================================================
SECTION 6: WORKFLOW RULES
================================================================================

SUMMARY: No workflow rules found in the scan data.

The system appears to rely on:
  - Validation rules (4 found in Deals)
  - Manual processes
  - Possible automation via Zoho Flow (not captured in this scan)
  - Stage transitions via UI

RECOMMENDATION: Consider implementing workflows for:
  - Automatic status updates on delivery
  - Payment reminders
  - Document requirement reminders
  - Approval gates at key stages


================================================================================
SECTION 7: KEY PICKLIST VALUES
================================================================================

7.1 DEAL STAGES (29 values - Complex Pipeline)
================================================================================
1. Qualification - Initial qualification
2. Identify Decision Makers - Decision maker identification
3. Needs Analysis - Customer needs assessment
4. Specifying - Technical specification phase
5. Value Proposition - Value proposition development
6. Negotiation/Review - Negotiation phase
7. Deal Won - Deal accepted by customer
8. Delivery/Claims - Active delivery/service phase
9. Closed Won - Deal completed successfully
10. Closed Lost - Deal lost
11. Closed-Lost to Competition - Lost to competitor
12. Delivery - Delivery in progress
13. Needs Evaluation - Alternative needs evaluation
14. Solution Design - Technical solution design
15. Pre Application - Pre-application phase (regulatory)
16. Fulfilment - Order fulfillment phase
17. New - New deal entry
18. Feedback - Feedback collection phase
19. Delivered - Fully delivered stage
20. Onboarding - Customer onboarding
21. CAS - Coordinated Application System
22. ST & NEM - Suruhanjaya Tenaga & Net Energy Metering
23. Tender - Tender/bidding phase
24. ST & TNB - Suruhanjaya Tenaga & Tenaga Nasional Berhad
25. Idle - Inactive/stalled deal
26. Site Assessment - Site assessment phase
27. Variation Order - Variation order processing
28. Reactivate - Deal reactivation
29. Retention - Retention/service phase

ANALYSIS:
- Multiple "Closed" variations (Won/Lost/Competition)
- Regulatory stages specific to Malaysia (CAS, ST & NEM, ST & TNB, NEM)
- Service/support stages (Onboarding, Feedback, Retention)
- Project phases (Qualification through Delivery)
- Recovery stages (Idle, Reactivate)

7.2 PROJECT TYPE PICKLIST
================================================================================
- -None-
- Housing
- Commercial
- Industrial
- Public
- Partner
- Residential

7.3 VOLTAGE TYPE PICKLIST (Electrical)
================================================================================
- -None-
- Single Phase
- Three Phase

7.4 SUPPLY OUTLET SIZE PICKLIST (Plumbing/Water)
================================================================================
- -None-
- 1/2 inch
- 3/4 inch
- 1 inch
- 1.5 inch
- 2 inch

7.5 ROOF TYPE PICKLIST (Solar Installation)
================================================================================
- -None-
- Tiles
- Flat Concrete Roof
- Flat Metal Roof
- MIX Tiles and Flat Metal Roof
- MIX Flat Metal and Flat Concrete Roof
- MIX Tiles and Flat Concrete Roof
- Metal Roof Klip-lok 700
- Metal Roof Klip-lok 406
- Metal Roof Standing Seam
- Shingle
- Structure

7.6 NEM SUBMISSION STATUS PICKLIST
================================================================================
- -None-
- NEM: Submitted
- NEM: Query
- NEM: Pass
- NEM: Pending
- NEM: Ready

7.7 ROOF LOAD EVALUATION PICKLIST
================================================================================
- -None-
- Able to Support
- Need Reinforcement
- Not Relevant
- Unable to install

7.8 DEAL TYPE PICKLIST
================================================================================
- -None-
- Development Project
- Partners
- Project (End)
- Commercial

7.9 PAYMENT METHOD PICKLIST
================================================================================
- -None-
- Cash
- 12 Month Instalment
- 24 Month instalment
- 36 Month Instalment
- 60 Month Instalment
- 48 Month Instalment

7.10 TNB TARIFF CATEGORY PICKLIST (Malaysian Utility)
================================================================================
- -None-
- B
- C1
- C2
- C3
- C4
- D
- E1
- E2
- E3

7.11 HEATER TYPE PICKLIST
================================================================================
- -None-
- Solar
- Solar PV
- Storage
- Heat Pump
- Hybrid Heater (Solar n Heat Pump)

7.12 SPECIAL DISCOUNTS/PROGRAMS PICKLIST
================================================================================
- -None-
- Charity
- Staff Gift
- Relationship Sales
- Collection After Delivery
- Collection After Commission
- Collection After Application

7.13 COMMUNITY PROJECT PICKLIST
================================================================================
- -None-
- Eco Ardence - Cora
- Eco Sanctuary - Monterey

7.14 RISK LEVEL PICKLIST
================================================================================
- -None-
- Low
- Medium
- High

7.15 TERMS & CONDITIONS - CATEGORY PICKLIST
================================================================================
- -None-
- Payment Terms
- Delivery Terms
- Confirmation Terms

7.16 TERMS & CONDITIONS - PAYMENT TERM PICKLIST
================================================================================
- -None-
- Cash on Delivery
- Cash before Delivery
- Cash on Installation
- Net 30 on Delivery
- Net 45 on Delivery
- Net 60 on Delivery
- Net 90 on Delivery

7.17 TERMS & CONDITIONS - USAGE TYPE PICKLIST
================================================================================
- -None-
- B2B
- B2C
- B2B and B2C

7.18 TERMS & CONDITIONS - ACTIVE PICKLIST
================================================================================
- -None-
- Yes
- No


================================================================================
SECTION 8: MODULE STATISTICS SUMMARY
================================================================================

MODULE BREAKDOWN:
  1. Deals                  - 204 fields,  21 related lists
  2. Quotes                 - 74 fields,   17 related lists
  3. Sales_Orders           - 53 fields,   14 related lists
  4. Invoices               - 101 fields,   9 related lists
  5. Products               - 36 fields,   19 related lists
  6. Contacts               - 44 fields,   16 related lists
  7. Accounts               - 55 fields,    9 related lists
  8. Terms_and_Conditions   - 23 fields,   24 related lists
  9. Delivery_Orders        - 29 fields,    6 related lists
  10. Housing_Developments  - 22 fields,    6 related lists
  11. PV_ROI_Table          - 119 fields,   6 related lists

TOTAL STATISTICS:
  - Total Fields Scanned: 560+
  - Total Custom Fields: 176 (in Deals alone)
  - Total Layouts: 4 (in Deals)
  - Total Validation Rules: 4 (in Deals)
  - Total Workflow Rules: 0
  - Total Related Lists: 148+ across all modules
  - Total Lookup Relationships: 50+
  - Total Picklist Fields: 100+


================================================================================
SECTION 9: BUSINESS PROCESS INSIGHTS
================================================================================

9.1 CORE BUSINESS MODEL
================================================================================
This CRM primarily supports:

1. SOLAR & RENEWABLE ENERGY INSTALLATION
   - System sizing (kWp, kWac)
   - Roof assessment and reinforcement
   - Inverter and module selection
   - ROI calculations
   - NEM (Net Energy Metering) tracking
   - TNB (Tenaga Nasional Berhad - Malaysian utility) integration

2. WATER SYSTEMS & HEATING
   - Water filter installation (POE, POU)
   - Heater types (Solar, Storage, Heat Pump, Hybrid)
   - Water quality concerns tracking
   - Pressure management

3. PROJECT-BASED DELIVERY
   - Multiple deal types (Housing, Commercial, Industrial, etc.)
   - Housing Development parent projects
   - Variation orders (VO) for scope changes
   - Milestone tracking (Truss, Roof, Electrical, etc.)

4. COMPLEX PAYMENT STRUCTURES
   - Multiple payment terms (Cash, 12/24/36/48/60 month installments)
   - Deposit and retention tracking
   - Collection management
   - Interest calculations (3.5% to 10% for various terms)

9.2 REGULATORY COMPLIANCE FOCUS
================================================================================
The system tracks:
- CAS (Coordinated Application System)
- NEM (Net Energy Metering) submission and approval
- ST & TNB (Suruhanjaya Tenaga & TNB) processes
- Technical documentation requirements
- Site assessments and structural evaluations

9.3 QUALITY & WARRANTY MANAGEMENT
================================================================================
- Defect tracking and reporting
- Defects Liability Period (DLP) tracking
- Certificate of Practical Completion (CPC)
- End date of liability period
- Service/maintenance tracking

9.4 FINANCIAL TRACKING
================================================================================
- Deal value estimation
- Contract sum tracking
- Variation orders
- Payment collections
- Delivery amounts
- Retention and deposit management
- ROI calculations for solar systems
- Savings estimation

9.5 DOCUMENTATION REQUIREMENTS
================================================================================
Multiple document types tracked via picklists:
- Roof plans (draft and final)
- Single line electrical drawings
- PVsyst simulation reports
- Site plans
- Technical specifications
- TNB documentation
- Regulatory forms (RJO, CAS Study)
- Load profile forms

9.6 GEOLOCATION & ADDRESS TRACKING
================================================================================
- Deal geolocation (latitude/longitude)
- Multiple address fields (shipping address in Delivery_Orders)
- Housing development location tracking
- Site-specific information


================================================================================
SECTION 10: RECOMMENDATIONS FOR IMPROVEMENT
================================================================================

10.1 WORKFLOW AUTOMATION OPPORTUNITIES
================================================================================
Current State: 0 workflow rules found
Recommendation: Implement workflows for:

1. Status Progression Automation
   - Auto-mark "Delivery/Claims" when first delivery created
   - Auto-mark "Fully Delivered" when all delivery orders completed
   - Auto-mark "Closed Won" when fully paid and delivered

2. Notification Workflows
   - Notify on payment due dates
   - Reminder for documentation uploads
   - Alert when deal in "Idle" for 30+ days

3. Document Management
   - Auto-create document checklist based on project type
   - Require signatures before stage transitions
   - Track document upload dates

4. Payment Tracking
   - Auto-calculate days overdue
   - Send payment reminders
   - Escalate overdue collections

10.2 BLUEPRINT IMPLEMENTATION
================================================================================
Current State: No blueprint configured
Recommendation: Create stage-transition blueprints for each deal type:

1. Housing/Residential Blueprint
   - Qualification → Site Assessment → Needs Analysis → Design →
   - Tender/Quotation → Deal Won → CAS Submission → NEM Submission →
   - Installation → Delivery → Onboarding → Retention

2. Commercial/Industrial Blueprint
   - Qualification → Needs Analysis → Value Proposition →
   - Specification → Negotiation → Deal Won → Fulfillment →
   - Delivery → Onboarding

3. Partner/Reseller Blueprint
   - Lead → Qualification → Quote → Deal Won → Support

10.3 DATA QUALITY IMPROVEMENTS
================================================================================
Add required fields:
- Confirmation_Terms (currently optional)
- Risk_Level assessment
- Project_Type classification
- Deal_Type specification

10.4 TERMS & CONDITIONS OPTIMIZATION
================================================================================
- Document standard T&C templates by type
- Create pricing tiers with standard deposit/retention %
- Link payment terms to deal value ranges
- Create approval workflow for new T&C creation

10.5 REPORTING & ANALYTICS
================================================================================
Current system lacks:
- Pipeline reports by stage and timeline
- Collection aging analysis
- Project profitability tracking
- ROI actual vs. estimated comparison
- Warranty/defect tracking reports
- Regulatory submission tracking reports

10.6 INTEGRATION OPPORTUNITIES
================================================================================
- Zoho Inventory integration (field already present: Zoho_Inventory boolean)
- Zoho WorkDrive integration (fields present for Folder ID and URL)
- Zoho Sign integration (ZohoSign_Documents related list exists)
- NEM online submission API
- TNB billing integration

10.7 FIELD ORGANIZATION
================================================================================
Current: 204 fields in Deals module is overwhelming
Recommendation: Reorganize via Layouts by business process:
- Solar Layout (solar-specific fields)
- Water/Heating Layout (water system fields)
- Housing Development Layout (development-specific)
- General/Commercial Layout (common fields)
- Compliance Layout (regulatory fields)


================================================================================
END OF ANALYSIS REPORT
================================================================================

This scan reveals a sophisticated CRM system designed for renewable energy and
home improvement projects with significant regulatory requirements, complex
payment structures, and multi-module interdependencies.

Key architectural strengths:
✓ Well-normalized Terms & Conditions master data
✓ Clear deal-to-delivery workflow
✓ Comprehensive lookup relationships
✓ Role-specific layouts
✓ Integration-ready (Workdrive, Sign, Inventory)

Opportunities for enhancement:
→ Blueprint workflows for stage gating
→ Workflow rules for automation
→ Structured reporting capabilities
→ Data quality validation
→ Documentation workflow tracking
