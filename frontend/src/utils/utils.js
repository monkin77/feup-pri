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