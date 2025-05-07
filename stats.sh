#!/bin/bash
##Cardano Node Block Stats (for Guild Operators environments)
##Data is gathered from mostly local data, using Guild Operators scripts (cncli/cardano-cli/koios)
##This is quite inneficcient. You should probably not use this, but write your own using less queries, and arrays. I am not a dev.
##Gus

BLOCKLOG_DB="/opt/cardano/cnode/guild-db/blocklog/blocklog.db"
current_epoch=$(cardano-cli query tip --mainnet|grep epoch|awk -F ' ' '{print $2}'|sed 's/,//g')
total=$(sqlite3 "${BLOCKLOG_DB}" "SELECT * FROM blocklog WHERE epoch=$current_epoch;"|wc -l)
next_epoch=$((current_epoch+1))
confirmed=$(sqlite3 "${BLOCKLOG_DB}" "SELECT * FROM blocklog WHERE epoch=$current_epoch;"|grep confirmed|wc -l)
leader=$(sqlite3 "${BLOCKLOG_DB}" "SELECT * FROM blocklog WHERE epoch=$current_epoch;"|grep leader|wc -l)
stolen=$(sqlite3 "${BLOCKLOG_DB}" "SELECT * FROM blocklog WHERE epoch=$current_epoch;"|grep -e ghosted -e stolen -e missed|wc -l)
adopted=$(sqlite3 "${BLOCKLOG_DB}" "SELECT * FROM blocklog WHERE epoch=$current_epoch;"|grep adopted|wc -l)
next_epoch_blocks=$(sqlite3 "${BLOCKLOG_DB}" "SELECT * FROM blocklog WHERE epoch=$next_epoch;"|grep leader|wc -l)
livestake=$(curl -sSL -f -X POST -H "Content-Type: application/json" -d '{"_pool_bech32_ids":["pool1example6rx0wv5gry4qx5l4h65qpjf7x99xmq66nqj2fj5gzzzz"]}' "https://api.koios.rest/api/v1/pool_info"|awk -F "," '{print $43}'|awk -F '"' '{print $4}'| rev | cut -c7- | rev|numfmt --grouping)

echo ""
echo "Current Epoch: $current_epoch"
echo "Blocks Assigned: $total"
echo "Blocks Confirmed: $confirmed"
echo "Blocks Lost: $stolen"
echo "Blocks Remaining: $leader"
echo "Blocks awaiting confirmation: $adopted"
echo "Active Stake: $livestake"
echo ""

if [ $next_epoch_blocks != 0 ]; then
echo "Next Epoch: $next_epoch"
echo "Next Epoch Blocks: $next_epoch_blocks"
echo ""
echo ""
fi
