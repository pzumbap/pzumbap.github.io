--1) What are the names of our clients and when they did enter the facility?

SELECT CONCAT(ClientFName, ' ', ClientLName) AS "Client Name", ClientEntryDate 
	FROM Client
	ORDER BY 2 ASC;

--2) What types of crime did our clients commit?  Include both the crime type and the name of the client.

SELECT CONCAT(ClientFName, ' ', ClientLName) AS "Client Name", CRecType AS "Crime Type"
	FROM Client JOIN CriminalRecord ON Client.ClientID = CriminalRecord.ClientID;

--3) How long did it take for a client to be sentenced after they committed a crime?  Include the name of the client as well.

SELECT CONCAT(ClientFName, ' ', ClientLName) AS "Client Name", CRecType AS "Crime Type", DATEDIFF(month, CRecCommDate, CRecSentDate) AS "Waiting time to receive Sentence [Months]"
	FROM Client JOIN CriminalRecord ON Client.ClientID = CriminalRecord.ClientID;

--4) How many hours did our clients use each counseling service?  Include the name of the client and order the result alphabetically by the name of the counseling service.

SELECT CONCAT(ClientFName, ' ', ClientLName) AS "Client Name", CSFocus AS "Counseling Service", CUHrs AS "Hours Used"
	FROM Client JOIN CounselingUse ON Client.ClientID = CounselingUse.ClientID 
				JOIN CounselingService ON CounselingUse.CSID = CounselingService.CSID
	ORDER BY 2 ASC;

--5) How often did our clients use each counseling service?  Order the results by the frequency with which the counseling services were used with the most frequently used one first.

SELECT CONCAT(ClientFName, ' ', ClientLName) AS "Client Name", CSFocus AS 'Counseling Service', COUNT(*) AS 'Frequency Counceling Service Used'
	FROM Client JOIN CounselingUse ON Client.ClientID = CounselingUse.ClientID
				JOIN CounselingService ON CounselingUse.CSID = CounselingService.CSID
	GROUP BY CONCAT(ClientFName, ' ', ClientLName), CSFocus
	ORDER BY 3 DESC;

--6) What is the average length of the sentences our clients received?  

SELECT AVG(CRecSentLen) AS "Average Length of Sentence [Months]" FROM CriminalRecord;

--7) Which companies hired clients?  Include both the company name and the name of the client.

SELECT CONCAT(ClientFName, ' ', ClientLName) AS "Hired Clients", Company AS 'Company Name'
	FROM Client JOIN JobApplication ON Client.ClientID = JobApplication.ClientID
				JOIN JobOpening ON JobApplication.JobID = JobOpening.JobID
	WHERE JAAppStatus = 'Hired';

--8) What are the names and sentence lengths of the clients and their scores on the courses they completed?  Include the CourseID as well.
-- Assumption: If the CrsCmplDateCompleted is NULL, that means a client has not completed the course yet. 

SELECT CONCAT(ClientFName, ' ', ClientLName) AS "Client Name", CRecSentLen AS 'Sentence Length [Months]', CrsComplCourseGrade AS 'Course Grade', CrsCmplBehGrade AS 'Behavioral Grade', CrsName AS "Course ID"
	FROM Client JOIN CourseCompletion ON Client.ClientID = CourseCompletion.ClientID
				JOIN CriminalRecord ON Client.ClientID = CriminalRecord.ClientID
				JOIN Course ON CourseCompletion.CrsID = Course.CrsID
	WHERE CrsCmplDateCompleted IS NOT NULL
	ORDER BY 3 ASC;






