import React, { useState, useEffect } from "react";
import {
    Autocomplete,
    FormControlLabel,
    Grid,
    IconButton,
    InputAdornment,
    Radio,
    RadioGroup,
    TextField,
    Typography,
} from "@mui/material";
import { Search as SearchIcon, Tune as TuneIcon } from "@mui/icons-material";
import { Stylesheet } from "../styles/stylesheet";
import { useNavigate } from "react-router-dom";
import { getSuggestion } from "../controller/solr";
import { queryOperations } from "../utils/utils";
import { ConfigSlider } from "../components/ConfigSlider";

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
    searchContainer: {
        display: "flex",
        width: "100%",
        flexDirection: "row",
        justifyContent: "center",
    },
    tuneIcon: {
        marginLeft: 5,
    },
    configField: {
        display: "flex",
        flexDirection: "row",
        marginTop: 15,
    },
    configContainer: {
        width: "40%",
        marginTop: 20,
        padding: 20,
        borderRadius: 20,
        // backgroundColor: "lightGray",
        border: "solid",
        borderWidth: 2,
    },
    configInput: {
        marginLeft: 20,
    },
    radioContainer: { marginLeft: 20 },
    configSection: {
        width: 120,
    },
};

export const HomePage = () => {
    const navigate = useNavigate();

    const [search, setSearch] = useState("");
    const [suggestions, setSuggestions] = useState([]);
    const [configOpen, setConfigOpen] = useState(false);
    const [fieldBoosts, setfieldBoosts] = useState({
        name: 1.0,
        industry: 1.0,
        description: 1.0,
    });
    const [numRows, setNumRows] = useState(10);
    const [queryOp, setQueryOp] = useState(queryOperations.OR);
    const [offset, setOffset] = useState(0);

    useEffect(() => {}, []);

    const onChangeSearch = async (event) => {
        setSearch(event.target.value);
        const newSuggestions = await getSuggestion(event.target.value);
        if (newSuggestions.ok) {
            setSuggestions(newSuggestions.data);
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        navigate("/results", {
            state: {
                searchValue: search,
                fieldBoosts,
                numRows,
                queryOp,
                offset,
            },
        });
    };

    const toggleConfig = () => setConfigOpen((prevValue) => !prevValue);

    const changeBoost = (boostKey, newVal) => {
        setfieldBoosts((prevValue) => ({
            ...prevValue,
            [boostKey]: newVal,
        }));
    };

    const handleOperationChange = (_, newVal) => {
        setQueryOp(newVal);
    };

    const changeNumRows = (evt) => {
        setNumRows(evt.target.value);
    };

    const changeOffset = (evt) => {
        setOffset(evt.target.value);
    };

    return (
        <>
            <div style={styles.container}>
                <div style={styles.centered}>
                    <h1 style={styles.title}>IndWish</h1>

                    <div style={styles.searchContainer}>
                        <form style={styles.searchBar} onSubmit={handleSubmit}>
                            <Autocomplete
                                disablePortal
                                id="combo-box-demo"
                                options={suggestions}
                                style={Stylesheet.fullWidth}
                                onChange={(event, value) => setSearch(value)}
                                freeSolo
                                renderInput={(params) => (
                                    <TextField
                                        {...params}
                                        id="searchBar"
                                        label="Search for Companies"
                                        variant="outlined"
                                        InputProps={{
                                            ...params.InputProps,
                                            autoComplete: "new-password", // disable autocomplete and autofill
                                            endAdornment: (
                                                <InputAdornment position="end">
                                                    <IconButton
                                                        onClick={handleSubmit}
                                                    >
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
                                )}
                            />
                        </form>

                        <IconButton
                            style={styles.tuneIcon}
                            onClick={toggleConfig}
                        >
                            <TuneIcon />
                        </IconButton>
                    </div>

                    {configOpen && (
                        <div style={styles.configContainer}>
                            <Grid container>
                                <Grid item xs={6}>
                                    <Typography variant="h5">
                                        Field Boosts
                                    </Typography>

                                    <ConfigSlider
                                        title="Name"
                                        field={fieldBoosts.name}
                                        fieldKey="name"
                                        onChange={changeBoost}
                                        min={0}
                                        max={4}
                                        step={0.25}
                                    />

                                    <ConfigSlider
                                        title="Industry"
                                        field={fieldBoosts.industry}
                                        fieldKey="industry"
                                        onChange={changeBoost}
                                        min={0}
                                        max={4}
                                        step={0.25}
                                    />

                                    <ConfigSlider
                                        title="Description"
                                        field={fieldBoosts.description}
                                        fieldKey="description"
                                        onChange={changeBoost}
                                        min={0}
                                        max={4}
                                        step={0.25}
                                    />
                                </Grid>

                                <Grid item xs={6}>
                                    <div style={Stylesheet.flexRow}>
                                        <Typography
                                            variant="h5"
                                            style={styles.configSection}
                                        >
                                            Operation
                                        </Typography>

                                        <RadioGroup
                                            aria-labelledby="demo-controlled-radio-buttons-group"
                                            name="controlled-radio-buttons-group"
                                            row
                                            value={queryOp}
                                            onChange={handleOperationChange}
                                            style={styles.radioContainer}
                                        >
                                            <FormControlLabel
                                                value={queryOperations.OR}
                                                control={<Radio />}
                                                label={queryOperations.OR}
                                            />
                                            <FormControlLabel
                                                value={queryOperations.AND}
                                                control={<Radio />}
                                                label={queryOperations.AND}
                                            />
                                        </RadioGroup>
                                    </div>

                                    <div style={styles.configField}>
                                        <Typography
                                            variant="h5"
                                            style={styles.configSection}
                                        >
                                            Results
                                        </Typography>

                                        <TextField
                                            id="numResultsInput"
                                            label="Number of Results"
                                            variant="outlined"
                                            style={styles.configInput}
                                            placeholder="Number of Results"
                                            color="primary"
                                            value={numRows}
                                            onChange={changeNumRows}
                                            size="small"
                                        />
                                    </div>

                                    <div style={styles.configField}>
                                        <Typography
                                            variant="h5"
                                            style={styles.configSection}
                                        >
                                            Offset
                                        </Typography>

                                        <TextField
                                            id="offsetInput"
                                            label="Search Offset"
                                            variant="outlined"
                                            style={styles.configInput}
                                            placeholder="Offset"
                                            color="primary"
                                            value={offset}
                                            onChange={changeOffset}
                                            size="small"
                                        />
                                    </div>
                                </Grid>
                            </Grid>
                        </div>
                    )}
                </div>
            </div>
        </>
    );
};
