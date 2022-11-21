const BACKEND_URL = process.env.REACT_APP_BACKEND_URL ?? "http://localhost:8080";

/**
 * 
 * @param {Item} item 
 * @returns {ok: boolean, data: data, err: string}
 */
export const setDone = async(item) => {
    try {
        const response = await fetch(`${BACKEND_URL}/todo/${item.id}/archive`, {
            method: 'PUT',
        });

        if (!response.ok) {
            return { ok: false }
        }

        const data = await response.json();
        return { ok: true, data: data };
    } catch (err) {
        return { ok: false, err: err };
    }
}