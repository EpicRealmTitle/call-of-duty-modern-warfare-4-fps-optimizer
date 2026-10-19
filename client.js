// Config module: client

const SETTINGS = {
    cwmwa: 903,
    hrqfb: 835,
    xlfht: 496,
    vjqz: 567,
};

function get(key, fallback) {
    return key in SETTINGS ? SETTINGS[key] : fallback;
}

module.exports = { SETTINGS, get };
