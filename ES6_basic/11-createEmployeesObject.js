// Write a function named createEmployeesObject that will receive two arguments: one string and one array

export default function createEmployeesObject(departmentName, employees) {
    return {
    [`${departmentName}`]: employees,
    };
}
