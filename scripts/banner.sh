#!/bin/bash

### [BANNER] ####
# Define colors
GREEN='\033[0;32m'
RED='\033[38;2;169;41;64m'
WHITE='\033[0;37m'
NC='\033[0m' # No Color
BOLD='\033[1m'


# Calculate terminal width
term_width=$(tput cols)

# Calculate left padding
left_padding=$(( (term_width - 59) / 2 ))

# Calculate left padding for the center text
center_text="Trəmpo: TRAnsMembrane Protein Order"
center_left_padding=$(( (term_width - ${#center_text}) / 2 ))

# Print the styled header with center alignment
printf "\n\n\n"

# Print the colored text with vertical slices
printf "%*s${WHITE}      ██╗ ██╗${GREEN}████████╗██████╗ ${WHITE} █████╗ ███╗   ███╗${RED}██████╗  ██████╗${WHITE}     ██╗ ██╗\n" $left_padding ""
printf "%*s${WHITE}     ██╔╝██╔╝╚══${GREEN}██╔══╝██╔══██╗${WHITE}██╔══██╗████╗ ████║${RED}██╔══██╗██╔═══██╗${WHITE}   ██╔╝██╔╝\n" $left_padding ""
printf "%*s${WHITE}    ██╔╝██╔╝   ${GREEN} ██║   ██████╔╝${WHITE}███████║██╔████╔██║${RED}██████╔╝██║   ██║${WHITE}  ██╔╝██╔╝\n" $left_padding ""
printf "%*s${WHITE}   ██╔╝██╔╝    ${GREEN} ██║   ██╔══██╗${WHITE}██╔══██║██║╚██╔╝██║${RED}██╔═══╝ ██║   ██║${WHITE} ██╔╝██╔╝\n" $left_padding ""
printf "%*s${WHITE}  ██╔╝██╔╝     ${GREEN} ██║   ██║  ██║${WHITE}██║  ██║██║ ╚═╝ ██║${RED}██║     ╚██████╔╝${WHITE}██╔╝██╔╝\n" $left_padding ""
printf "%*s${WHITE}  ╚═╝ ╚═╝      ${GREEN} ╚═╝   ╚═╝  ╚═╝${WHITE}╚═╝  ╚═╝╚═╝     ╚═╝${RED}╚═╝      ╚═════╝${WHITE} ╚═╝ ╚═╝ ${NC}\n" $left_padding
echo ""

echo ""
printf "${BOLD}%*s TRAMPO: TRAnsMembrane Protein Order${NC}\n" $center_left_padding ""
echo ""
echo ""
