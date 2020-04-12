
def estimator(data):
  {
    data= {
      "region = {
      "name": "Africa",
      "avgAge": 19.7,
      "avgDailyIncomeInUSD": 5, #*4
      "avgDailyIncomePopulation" :0.71  #*.73
    },
    periodType: "days",
    timeToElapse: 58,
    reportedCases: 674,
    population: 66622705,
    totalHospitalBeds: 1380614
    }, 
    estimate: {
    impact: {
      currentlyInfected: reportedCases * 10, #impact.currentlyInfected
      infectionsByRequestedTime: currentlyInfected  * (2**9 ),
      severeCasesByRequestedTime: infectionsByRequestedTime * .15, #severe positive cases require hospitalisation to recover
      hospitalBedsByRequestedTime:  (totalHospitalBeds * .35)- severeCasesByRequestedTime,     casesForICUByRequestedTime: infectionsByRequestedTime * .05, #require ICU care
      casesForVentilatorsByRequestedTime: infectionsByRequestedTime * .02, #require ventilator
      dollarsInFlight: infectionsByRequestedTime *0.65 * 1.5 * 30, #*2 decimal places   dollarInFlight = Math.trunc((infectionByRequestedTime * avgDailyinUSD * avgDailyPopulation)/noOfDays)
    }, 

    severeImpact: {
      currentlyInfected: reportedCases * 50, #severeImpact.currentlyInfected
      infectionsByRequestedTime: currentlyInfected * (2**9),
      severeCasesByRequestedTime: infectionsByRequestedTime * .15, 
      hospitalBedsByRequestedTime: totalHospitalBeds * 35 - severeCasesByRequestedTime,
      casesForICUByRequestedTime: infectionsByRequestedTime * .05, #require ICU care
      casesForVentilatorsByRequestedTime: infectionsByRequestedTime *.02, #require ventilator
      dollarsInFlight: (currentlyInfected * 0.65) * 1.5 , 

    } 
  }
  return (data)