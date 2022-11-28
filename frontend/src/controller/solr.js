const BACKEND_URL = process.env.REACT_APP_BACKEND_URL ?? "http://localhost:8983";

/**
 * 
 * @param {string} query 
 * @returns {ok: boolean, data: data, err: string}
 */
export const querySolr = async(query) => {
    try {
        // TODO: Additional params  &qf=name+industry+description&rows=10
        const response = await fetch(`${BACKEND_URL}/solr/reviews/select?_=1668256462851&defType=edismax&indent=true&q=${query}&q.op=OR`, {
            method: 'GET',
        });

        if (!response.ok) {
            return { ok: false }
        }

        let data = await response.json();
        data = data.response;
        return { ok: true, data: data };
    } catch (err) {
        return { ok: false, err: err };
    }
}