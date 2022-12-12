// Convert a string to 32bit integer
export function stringToHash(string) {
    let hash = 0;

    if (string.length === 0) return hash;

    for (let i = 0; i < string.length; i++) {
        const char = string.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }

    return hash.toString();
}

/**
 * 
 * @param {*} company 
 * @returns [List, avg] List of Perks and their ratings [{name: "perk1", rating: 4}, {name: "perk2", rating: 5}}]
 */
export const getPerksRatings = (company) => {
    const perksKeys = Object.keys(company).filter((key) =>
        key.startsWith("ratings.")
    );
    const perksRatings = [];
    for (const key of perksKeys) {
        perksRatings.push({
            name: key.split(".")[1],
            rating: company[key],
        });
    }

    let avgPerksRating = perksKeys.reduce(
        (accumulator, currPerk) => accumulator + company[currPerk],
        0
    );
    avgPerksRating = avgPerksRating / perksKeys.length;
    avgPerksRating = avgPerksRating.toFixed(2);
    if (avgPerksRating === "NaN") avgPerksRating = null;

    return [perksRatings, avgPerksRating];
}


/**
 * 
 * @param {*} company 
 * @returns [List, avg] List of Happiness and their ratings [{name: "perk1", rating: 4}, {name: "perk2", rating: 5}}]
 */
export const getHappinessRatings = (company) => {
    const happinessKeys = Object.keys(company).filter((key) =>
        key.startsWith("happiness.")
    );
    const happinessRatings = [];
    for (const key of happinessKeys) {
        happinessRatings.push({
            name: key.split(".")[1],
            rating: company[key],
        });
    }

    let avgHappinessRatings = happinessKeys.reduce(
        (accumulator, currPerk) => accumulator + company[currPerk],
        0
    );
    avgHappinessRatings = avgHappinessRatings / happinessKeys.length;
    avgHappinessRatings = avgHappinessRatings.toFixed(2);
    if (avgHappinessRatings === "NaN") avgHappinessRatings = null;

    return [happinessRatings, avgHappinessRatings];
}

/**
 * 
 * @param {*} company 
 * @returns [List, avg] List of Roles and their ratings [{name: "perk1", rating: 4}, {name: "perk2", rating: 5}}]
 */
export const getRolesRatings = (company) => {
    const rolesKeys = Object.keys(company).filter((key) =>
        key.startsWith("roles.")
    );
    const rolesRating = [];
    for (const key of rolesKeys) {
        rolesRating.push({
            name: key.split(".")[1],
            rating: company[key],
        });
    }

    let avgRolesRating = rolesKeys.reduce(
        (accumulator, currPerk) => accumulator + company[currPerk],
        0
    );
    avgRolesRating = avgRolesRating / rolesKeys.length;
    avgRolesRating = avgRolesRating.toFixed(2);
    if (avgRolesRating === "NaN") avgRolesRating = null;

    return [rolesRating, avgRolesRating];
}

/**
 * 
 * @param {*} company 
 * @returns [List, avg] List of Roles and their salaries [{name: "perk1", salary: 4}, {name: "perk2", salary: 5}}]
 */
export const getRolesSalary = (company) => {
    const rolesKeys = Object.keys(company).filter((key) =>
        key.startsWith("salary.")
    );
    const rolesSalary = [];
    for (const key of rolesKeys) {
        rolesSalary.push({
            name: key.split(".")[1],
            salary: company[key],
        });
    }

    let avgRolesSalary = rolesKeys.reduce(
        (accumulator, currPerk) => accumulator + company[currPerk],
        0
    );
    avgRolesSalary = avgRolesSalary / rolesKeys.length;
    avgRolesSalary = avgRolesSalary.toFixed(2);
    if (avgRolesSalary === "NaN") avgRolesSalary = null;

    return [rolesSalary, avgRolesSalary];
}


/**
 * 
 * @param {*} company 
 * @returns List of Interview data and their values {difficulty: "Easy", duration: "About a day or two"}
 */
export const getInterviewData = (company) => {
    const interviewKeys = Object.keys(company).filter((key) =>
        key.startsWith("interview.")
    );
    const interviewData = {};
    for (const key of interviewKeys) {
        interviewData[key.split(".")[1]] = company[key];

    }

    return interviewData;
}

export const employeeMapper = {
    1: "1",
    2: "2 to 10",
    3: "11 to 50",
    4: "51 to 200",
    5: "201 to 500",
    6: "501 to 1,000",
    7: "1,001 to 5,000",
    8: "5,001 to 10,000",
    9: "10,000+"
};

export const revenueMapper = {
    1: "less than $1M (USD)",
    2: "$1M to $5M (USD)",
    3: "$5M to $25M (USD)",
    4: "$25M to $100M (USD)",
    5: "$100M to $500M (USD)",
    6: "$500M to $1B (USD)",
    7: "$1B to $5B (USD)",
    8: "$5B to $10B (USD)",
    9: "more than $10B (USD)"
};

export const queryOperations = {
    AND: "AND",
    OR: "OR"
};