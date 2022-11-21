import React, { useState, useEffect } from "react";
import { Grid, Typography } from "@mui/material";
import { TodoCard } from "../components/TodoCard";
import { Item, itemStates } from "../model/Item";
import { setDone } from "../controller/todoItems";

const styles = {
    container: {
        padding: "1rem",
        minHeight: "100vh",
        backgroundColor: "lightBlue",
        boxSizing: "border-box",
    },
    column: {
        width: "85%",
        margin: "auto",
        backgroundColor: "lightGrey",
        padding: "2rem",
        borderRadius: "1rem",
        minHeight: "50vh",
    },
};

const dummyItems = [
    new Item("task 1", itemStates.todo),
    new Item("task 2", itemStates.done),
];

// Optional TODO: Make The App pretty *-*

/* Optional TODO: Create an app global state (redux) containing a 'loading' flag. 
While backend requests are being processed, show the loading indicator in the UI */

export const HomePage = () => {
    /**
     * TODO nº1: Initialize items as an empty list
     */
    const [items, setItems] = useState(dummyItems);

    useEffect(() => {
        /* TODO nº2: Fetch items from the backend and 
        update the items variable with the result */
    }, []);

    const handleDone = async (item) => {
        const result = await setDone(item);

        if (!result.ok) {
            // Failed request
            console.log("Error setting item to done.");
            return;
        }

        // Updating state to Done in the UI
        const newItems = items.map((currItem) => {
            if (currItem.id === item.id) currItem.state = itemStates.done;
            return currItem;
        });
        setItems(newItems);
    };

    return (
        <div style={styles.container}>
            <h1>Indwish</h1>
            <Grid container padding={2}>
                <Grid item xs={12} md={6} style={styles.grid} paddingBottom={3}>
                    <div style={styles.column}>
                        <Typography variant="h2">Todo</Typography>

                        <TodoCard
                            title="TODO"
                            items={
                                items /* TODO nº3: filter the items with state TODO */
                            }
                            handleDone={handleDone}
                        />
                    </div>
                </Grid>

                <Grid item xs={12} md={6}>
                    <div style={styles.column}>
                        <Typography variant="h2">Done</Typography>

                        {/* TODO nº4: Add Card for Tasks done  */}
                    </div>
                </Grid>
            </Grid>
        </div>
    );
};
