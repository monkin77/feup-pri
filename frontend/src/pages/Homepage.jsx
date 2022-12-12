import React, { useState, useEffect } from "react";
import { Autocomplete, IconButton, InputAdornment, TextField } from "@mui/material";
import { Search as SearchIcon } from "@mui/icons-material";
import { Stylesheet } from "../styles/stylesheet";
import {useNavigate} from 'react-router-dom'
import { getSuggestion } from "../controller/solr";

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
        fontFamily: "Roboto",
    },
    searchBar: {
        width: "40%",
    },
};


export const HomePage = () => {
    const [search, setSearch] = useState("");
    const [suggestions, setSuggestions] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        
    }, []);

    const onChangeSearch = async (event) => {
        setSearch(event.target.value);
        const newSuggestions = await getSuggestion(event.target.value);
        if (newSuggestions.ok) {
            setSuggestions(newSuggestions.data);
        }
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        
        navigate("/results", { state: {searchValue: search} });
    };

    return (
        <>
            <div style={styles.container}>
                <div style={styles.centered}>
                    <h1 style={styles.title}>IndWish</h1>
                    <form style={styles.searchBar} onSubmit={handleSubmit}>
                        <Autocomplete
                            disablePortal
                            id="combo-box-demo"
                            options={suggestions}
                            style={Stylesheet.fullWidth}
                            onChange={(event, value) => setSearch(value)}
                            renderInput={(params) =>
                                <TextField
                                    {...params}
                                    id="searchBar"
                                    label="Search for Companies"
                                    variant="outlined"
                                    InputProps={{
                                        ...params.InputProps,
                                        autoComplete: 'new-password', // disable autocomplete and autofill
                                        endAdornment: (
                                            <InputAdornment position="end">
                                                <IconButton onClick={handleSubmit}>
                                                    <SearchIcon />
                                                </IconButton>
                                            </InputAdornment>
                                        ),
                                    }}
                                    placeholder="Search"
                                    color="primary"
                                    value={search}
                                    onChange={onChangeSearch}
                                    />
                                }
                            />
                    </form>
                </div>
            </div>
        </>
    );
};
