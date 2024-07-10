// Function named createIteratorObject, that will take into argument a report Object created with the previous function createReportObject

export default function createIteratorObject(report) {
    let result = [];
    for (const value of Object.values(report.allEmployees)) {
        result = [...result, ...value]
    }
    return result;
}