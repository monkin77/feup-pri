import { queryOperations } from "../utils/utils";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL ?? "http://localhost:8983";

/**
 * 
 * @param {string} query 
 * @returns {ok: boolean, data: data, err: string}
 */
export const querySolr = async(query, queryOp = queryOperations.OR, fieldBoosts = null, numberResults = 10, offset = 0) => {
    try {
        // TODO: Test this query. Before it was name%20industry%20description
        let queryFields = "name industry description";
        if (fieldBoosts) {
            queryFields = `name^${fieldBoosts.name} industry^${fieldBoosts.industry} description^${fieldBoosts.description}`;
        }

        const reqUrl = `${BACKEND_URL}/solr/reviews/select?defType=edismax&indent=true&q.op=${queryOp}&q=${query}&
qf=${queryFields}&rows=${numberResults}&start=${offset}`;

        const response = await fetch(reqUrl, {
            method: 'GET',
        });

        if (!response.ok) {
            return { ok: false, err: response };
        }

        let data = await response.json();
        data = data.response;
        return { ok: true, data: data };
    } catch (err) {
        return { ok: false, err: err };
    }
}

/**
 * Gets suggestion for the query from solr
 * @param {*} query
 * @returns {ok: boolean, data: data, err: string}
 */
export const getSuggestion = async (query) => {
    try {
        const response = await fetch(`${BACKEND_URL}/solr/reviews/suggest?q=${query}&wt=json`, {
            method: 'GET',
        });

        if (!response.ok) {
            return { ok: false, err: response };
        }

        let data = await response.json();
        data = data.suggest.reviewsSuggester[query].suggestions;
        data = data.map((suggestion) => suggestion.term);

        return { ok: true, data: data };
    } catch (err) {
        return { ok: false, err: err };
    }
}