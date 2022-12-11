const BACKEND_URL = process.env.REACT_APP_BACKEND_URL ?? "http://localhost:8983";

/**
 * 
 * @param {string} query 
 * @returns {ok: boolean, data: data, err: string}
 */
export const querySolr = async(query) => {
    try {
        // TODO: Additional params  &qf=name+industry+description&rows=10
        const response = await fetch(`${BACKEND_URL}/solr/reviews/select?defType=edismax&indent=true&q.op=OR&q=${query}&qf=name%20industry%20description&rows=10&start=0`, {
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