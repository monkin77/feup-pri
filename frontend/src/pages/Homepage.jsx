import React, { useState, useEffect } from "react";
import { Item, itemStates } from "../model/Item";
import { setDone } from "../controller/todoItems";
import { IconButton, InputAdornment, TextField } from "@mui/material";
import { Search as SearchIcon } from "@mui/icons-material";
import { Stylesheet } from "../styles/stylesheet";

const styles = {
    container: {
        padding: "1rem",
        minHeight: "100vh",
        backgroundColor: "lightBlue",
        boxSizing: "border-box",
        position: "relative",
        height: "100%",
    },
    centered: {
        display: "flex",
        flex: 1,
        height: "100%",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
    },
    title: {
        fontSize: "4rem",
    },
    searchBar: {
        width: "40%",
    },
};

const dummyItems = [
    new Item("task 1", itemStates.todo),
    new Item("task 2", itemStates.done),
];

export const HomePage = () => {
    /**
     * TODO nº1: Initialize items as an empty list
     */
    const [items, setItems] = useState(dummyItems);

    useEffect(() => {
        /* TODO nº2: Fetch items from the backend and 
        update the items variable with the result */
    }, []);

    const handleSubmit = (event) => {
        console.log(event);
        event.preventDefault();
    };

    return (
        <div style={styles.container}>
            <div style={styles.centered}>
                <h1 style={styles.title}>IndWish</h1>
                <form style={styles.searchBar} onSubmit={handleSubmit}>
                    <TextField
                        id="searchBar"
                        label="Search for Companies"
                        variant="outlined"
                        InputProps={{
                            endAdornment: (
                                <InputAdornment position="end">
                                    <IconButton onClick={handleSubmit}>
                                        <SearchIcon />
                                    </IconButton>
                                </InputAdornment>
                            ),
                        }}
                        style={Stylesheet.fullWidth}
                        placeholder="Search"
                        color="primary"
                    />
                </form>
            </div>
        </div>
    );
};
