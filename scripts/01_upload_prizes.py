# ACTUAL SCRIPT STARTS ON LINE 294

# This is a dict that maps a sponsor to their logo url (like the ones you see in the prizes section
# of a hackathon or the project cards in the showcase). I used another script and manual editing to create this.
imageUrls = {
    '/images/trophy.jpg': 'Unknown',
    'https://ethglobal.b-cdn.net/organizations/026zc/square-logo/default.png': 'Uniswap Foundation',
    'https://ethglobal.b-cdn.net/organizations/06qyw/square-logo/default.png': 'Shardeum',
    'https://ethglobal.b-cdn.net/organizations/0accc/square-logo/default.png': 'Nillion',
    'https://ethglobal.b-cdn.net/organizations/0k3eo/square-logo/default.png': 'Gelato Network',
    'https://ethglobal.b-cdn.net/organizations/0ndp2/square-logo/default.png': 'Hyperlane',
    'https://ethglobal.b-cdn.net/organizations/0p5er/square-logo/default.png': 'Neon EVM',
    'https://ethglobal.b-cdn.net/organizations/0q1p4/square-logo/default.png': 'Fleek',
    'https://ethglobal.b-cdn.net/organizations/0tx58/square-logo/default.png': '???', # Most likely Reflexer Labs, shoud've been trophy
    'https://ethglobal.b-cdn.net/organizations/0vx1d/square-logo/default.png': 'Mode Network',
    'https://ethglobal.b-cdn.net/organizations/0w2pp/square-logo/default.png': 'Aave',
    'https://ethglobal.b-cdn.net/organizations/10a1v/square-logo/default.png': 'Push Protocol',
    'https://ethglobal.b-cdn.net/organizations/1assb/square-logo/default.png': 'Lilypad',
    'https://ethglobal.b-cdn.net/organizations/1do5k/square-logo/default.png': 'Axiom',
    'https://ethglobal.b-cdn.net/organizations/1ijf8/square-logo/default.png': 'Oasis Protocol',
    'https://ethglobal.b-cdn.net/organizations/1kchc/square-logo/default.png': 'Airdao',
    'https://ethglobal.b-cdn.net/organizations/1nz66/square-logo/default.png': 'Li.Fi',
    'https://ethglobal.b-cdn.net/organizations/1pyem/square-logo/default.png': '???', # Most likely Flux, should've been trophy
    'https://ethglobal.b-cdn.net/organizations/24ige/square-logo/default.png': '???', # No project has this
    'https://ethglobal.b-cdn.net/organizations/26gjy/square-logo/default.png': 'Cronos',
    'https://ethglobal.b-cdn.net/organizations/2guk4/square-logo/default.png': 'DIMO',
    'https://ethglobal.b-cdn.net/organizations/2gzxu/square-logo/default.png': '???', # Most likely Gnosis Safe, should've been trophy
    'https://ethglobal.b-cdn.net/organizations/2ixf3/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/2mig9/square-logo/default.png': 'Quantstamp',
    'https://ethglobal.b-cdn.net/organizations/2t2i9/square-logo/default.png': 'Farcaster',
    'https://ethglobal.b-cdn.net/organizations/2ugg8/square-logo/default.png': 'Flare Network',
    'https://ethglobal.b-cdn.net/organizations/2x9jd/square-logo/default.png': 'zkBob',
    'https://ethglobal.b-cdn.net/organizations/2zqzn/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/362vt/square-logo/default.png': 'Ethereum Foundation',
    'https://ethglobal.b-cdn.net/organizations/3gx1k/square-logo/default.png': 'thirdweb',
    'https://ethglobal.b-cdn.net/organizations/3kfd8/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/3pgwq/square-logo/default.png': 'Alluo',
    'https://ethglobal.b-cdn.net/organizations/3uuu9/square-logo/default.png': 'Threshold Network',
    'https://ethglobal.b-cdn.net/organizations/3wes0/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/3zpxc/square-logo/default.png': 'Worldcoin',
    'https://ethglobal.b-cdn.net/organizations/3zz4k/square-logo/default.png': 'Fraxtal',
    'https://ethglobal.b-cdn.net/organizations/42b0f/square-logo/default.png': 'WeatherXM',
    'https://ethglobal.b-cdn.net/organizations/4388j/square-logo/default.png': 'Starknet',
    'https://ethglobal.b-cdn.net/organizations/43ago/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/46q4i/square-logo/default.png': 'WalletConnect',
    'https://ethglobal.b-cdn.net/organizations/48dft/square-logo/default.png': 'Intmax',
    'https://ethglobal.b-cdn.net/organizations/493ck/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/4fmxr/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/4hh1n/square-logo/default.png': 'Bacalhau',
    'https://ethglobal.b-cdn.net/organizations/4hzt5/square-logo/default.png': 'Herodotus',
    'https://ethglobal.b-cdn.net/organizations/4i0qt/square-logo/default.png': 'Sismo',
    'https://ethglobal.b-cdn.net/organizations/4jgzz/square-logo/default.png': 'NFT.Storage',
    'https://ethglobal.b-cdn.net/organizations/4o3cq/square-logo/default.png': 'Conduit',
    'https://ethglobal.b-cdn.net/organizations/4pn9u/square-logo/default.png': 'MetaMask',
    'https://ethglobal.b-cdn.net/organizations/4uiut/square-logo/default.png': 'Metal L2',
    'https://ethglobal.b-cdn.net/organizations/4v3qj/square-logo/default.png': 'Karma3Labs',
    'https://ethglobal.b-cdn.net/organizations/5b69q/square-logo/default.png': 'NEAR Protocol',
    'https://ethglobal.b-cdn.net/organizations/5dgqn/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/5e2gc/square-logo/default.png': 'Curvegrid',
    'https://ethglobal.b-cdn.net/organizations/5mkws/square-logo/default.png': 'Capsule',
    'https://ethglobal.b-cdn.net/organizations/5neyp/square-logo/default.png': 'Pinata',
    'https://ethglobal.b-cdn.net/organizations/6absf/square-logo/default.png': 'Moonbeam',
    'https://ethglobal.b-cdn.net/organizations/6g24q/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/6hzdh/square-logo/default.png': 'Hyperbolic',
    'https://ethglobal.b-cdn.net/organizations/6ow0m/square-logo/default.png': 'Vara',
    'https://ethglobal.b-cdn.net/organizations/6wi0d/square-logo/default.png': 'Mina Protocol',
    'https://ethglobal.b-cdn.net/organizations/78tgi/square-logo/default.png': 'CoW Protocol',
    'https://ethglobal.b-cdn.net/organizations/79zf4/square-logo/default.png': 'UNICEF Innovation',
    'https://ethglobal.b-cdn.net/organizations/7go1p/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/7pft7/square-logo/default.png': 'Essential',
    'https://ethglobal.b-cdn.net/organizations/7z88g/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/814vz/square-logo/default.png': 'unshETH.xyz',
    'https://ethglobal.b-cdn.net/organizations/831ya/square-logo/default.png': 'Family',
    'https://ethglobal.b-cdn.net/organizations/88fj5/square-logo/default.png': 'Zerion',
    'https://ethglobal.b-cdn.net/organizations/8hucp/square-logo/default.png': 'Alliance',
    'https://ethglobal.b-cdn.net/organizations/8i5pu/square-logo/default.png': 'POAP',
    'https://ethglobal.b-cdn.net/organizations/8kguf/square-logo/default.png': 'Blockscout',
    'https://ethglobal.b-cdn.net/organizations/8o6ne/square-logo/default.png': 'DELV',
    'https://ethglobal.b-cdn.net/organizations/8un5e/square-logo/default.png': '0x',
    'https://ethglobal.b-cdn.net/organizations/8z5mg/square-logo/default.png': 'PancakeSwap',
    'https://ethglobal.b-cdn.net/organizations/910t9/square-logo/default.png': 'Avail',
    'https://ethglobal.b-cdn.net/organizations/92qx9/square-logo/default.png': 'vlayer Labs',
    'https://ethglobal.b-cdn.net/organizations/96nbu/square-logo/default.png': 'Aleo',
    'https://ethglobal.b-cdn.net/organizations/96pd9/square-logo/default.png': 'Ceramic',
    'https://ethglobal.b-cdn.net/organizations/992b8/square-logo/default.png': 'Ethereum Attestation Service',
    'https://ethglobal.b-cdn.net/organizations/9jtc3/square-logo/default.png': 'Argent',
    'https://ethglobal.b-cdn.net/organizations/9q77n/square-logo/default.png': 'NETH',
    'https://ethglobal.b-cdn.net/organizations/9xct6/square-logo/default.png': 'Gnosis',
    'https://ethglobal.b-cdn.net/organizations/9xedj/square-logo/default.png': 'Highlight',
    'https://ethglobal.b-cdn.net/organizations/9ysqe/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/9z8z1/square-logo/default.png': 'Gnosis Chain',
    'https://ethglobal.b-cdn.net/organizations/9zj01/square-logo/default.png': 'Filecoin',
    'https://ethglobal.b-cdn.net/organizations/a1him/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/aa2tg/square-logo/default.png': 'API3',
    'https://ethglobal.b-cdn.net/organizations/acypq/square-logo/default.png': 'Ripio',
    'https://ethglobal.b-cdn.net/organizations/am855/square-logo/default.png': 'Marlin',
    'https://ethglobal.b-cdn.net/organizations/av8vu/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/axdu9/square-logo/default.png': 'Risc Zero',
    'https://ethglobal.b-cdn.net/organizations/b2u1b/square-logo/default.png': 'Fluence',
    'https://ethglobal.b-cdn.net/organizations/bdi3h/square-logo/default.png': 'Hedera',
    'https://ethglobal.b-cdn.net/organizations/bht2g/square-logo/default.png': 'Reazon Holdings',
    'https://ethglobal.b-cdn.net/organizations/biwnb/square-logo/default.png': 'UNLIMIT',
    'https://ethglobal.b-cdn.net/organizations/bk5qx/square-logo/default.png': 'Nethermind',
    'https://ethglobal.b-cdn.net/organizations/bmhmf/square-logo/default.png': 'Tokenbound',
    'https://ethglobal.b-cdn.net/organizations/btkw6/square-logo/default.png': 'Certora',
    'https://ethglobal.b-cdn.net/organizations/buucz/square-logo/default.png': 'Cartesi',
    'https://ethglobal.b-cdn.net/organizations/bw7y9/square-logo/default.png': 'ENS',
    'https://ethglobal.b-cdn.net/organizations/c5jvk/square-logo/default.png': 'OKX Web3', # Assumption
    'https://ethglobal.b-cdn.net/organizations/ci5d7/square-logo/default.png': 'Rome Protocol',
    'https://ethglobal.b-cdn.net/organizations/croq1/square-logo/default.png': 'Fhenix',
    'https://ethglobal.b-cdn.net/organizations/cycii/square-logo/default.png': 'Iron Fish',
    'https://ethglobal.b-cdn.net/organizations/d09ed/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/dkzkp/square-logo/default.png': 'LayerZero',
    'https://ethglobal.b-cdn.net/organizations/e3t1p/square-logo/default.png': 'NounsDAO',
    'https://ethglobal.b-cdn.net/organizations/e8ob5/square-logo/default.png': 'OpenSea',
    'https://ethglobal.b-cdn.net/organizations/eirr9/square-logo/default.png': 'Goldsky',
    'https://ethglobal.b-cdn.net/organizations/enkg5/square-logo/default.png': 'StackOS',
    'https://ethglobal.b-cdn.net/organizations/eov0f/square-logo/default.png': 'Tableland',
    'https://ethglobal.b-cdn.net/organizations/eu794/square-logo/default.png': 'Inco Network',
    'https://ethglobal.b-cdn.net/organizations/f0wnx/square-logo/default.png': 'Token Flow',
    'https://ethglobal.b-cdn.net/organizations/f2so0/square-logo/default.png': 'Zora',
    'https://ethglobal.b-cdn.net/organizations/f5vjp/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/f7o0p/square-logo/default.png': 'Covalent',
    'https://ethglobal.b-cdn.net/organizations/f8ku2/square-logo/default.png': 'Chainlink',
    'https://ethglobal.b-cdn.net/organizations/fb98y/square-logo/default.png': 'Airstack',
    'https://ethglobal.b-cdn.net/organizations/fbyii/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/ffic2/square-logo/default.png': 'Liquity',
    'https://ethglobal.b-cdn.net/organizations/fimmp/square-logo/default.png': 'Squid Router',
    'https://ethglobal.b-cdn.net/organizations/fjaae/square-logo/default.png': 'Flow',
    'https://ethglobal.b-cdn.net/organizations/fk9gm/square-logo/default.png': 'Witness',
    'https://ethglobal.b-cdn.net/organizations/fn4k5/square-logo/default.png': 'Tenderly',
    'https://ethglobal.b-cdn.net/organizations/fp1x1/square-logo/default.png': 'UMA',
    'https://ethglobal.b-cdn.net/organizations/frkz3/square-logo/default.png': 'Cartridge',
    'https://ethglobal.b-cdn.net/organizations/fuytu/square-logo/default.png': 'Autonomy',
    'https://ethglobal.b-cdn.net/organizations/fxknf/square-logo/default.png': 'Gaia',
    'https://ethglobal.b-cdn.net/organizations/g3uvh/square-logo/default.png': 'Triangle',
    'https://ethglobal.b-cdn.net/organizations/g7h9m/square-logo/default.png': 'Pyth Network',
    'https://ethglobal.b-cdn.net/organizations/ggpyp/square-logo/default.png': 'Rootstock',
    'https://ethglobal.b-cdn.net/organizations/gs0z1/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/gt566/square-logo/default.png': 'Hyperlane',
    'https://ethglobal.b-cdn.net/organizations/h0nyy/square-logo/default.png': 'Sindri',
    'https://ethglobal.b-cdn.net/organizations/h24ko/square-logo/default.png': 'dabl.club',
    'https://ethglobal.b-cdn.net/organizations/h5ps8/square-logo/default.png': 'Base',
    'https://ethglobal.b-cdn.net/organizations/hcd86/square-logo/default.png': 'Morpho Labs',
    'https://ethglobal.b-cdn.net/organizations/hoadp/square-logo/default.png': 'Axelar',
    'https://ethglobal.b-cdn.net/organizations/hp48a/square-logo/default.png': 'Polybase',
    'https://ethglobal.b-cdn.net/organizations/i27s1/square-logo/default.png': 'Okto',
    'https://ethglobal.b-cdn.net/organizations/i6xez/square-logo/default.png': 'Findora',
    'https://ethglobal.b-cdn.net/organizations/i90pd/square-logo/default.png': 'Galadriel',
    'https://ethglobal.b-cdn.net/organizations/if0ri/square-logo/default.png': '1inch',
    'https://ethglobal.b-cdn.net/organizations/ijybm/square-logo/default.png': 'Privy',
    'https://ethglobal.b-cdn.net/organizations/ikmn9/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/inotq/square-logo/default.png': 'Celo',
    'https://ethglobal.b-cdn.net/organizations/iydyv/square-logo/default.png': 'Revise',
    'https://ethglobal.b-cdn.net/organizations/j5c6h/square-logo/default.png': 'Consensus Lab',
    'https://ethglobal.b-cdn.net/organizations/j5u2x/square-logo/default.png': 'Compound Grants Program',
    'https://ethglobal.b-cdn.net/organizations/j61b3/square-logo/default.png': 'Evmos',
    'https://ethglobal.b-cdn.net/organizations/jcyjn/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/jkakt/square-logo/default.png': 'Starton',
    'https://ethglobal.b-cdn.net/organizations/jkorc/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/juzwo/square-logo/default.png': 'Dune',
    'https://ethglobal.b-cdn.net/organizations/jwenb/square-logo/default.png': 'Saturn',
    'https://ethglobal.b-cdn.net/organizations/jxca4/square-logo/default.png': 'Blockless',
    'https://ethglobal.b-cdn.net/organizations/jywri/square-logo/default.png': 'QuickNode',
    'https://ethglobal.b-cdn.net/organizations/jzpj5/square-logo/default.png': 'Mantle',
    'https://ethglobal.b-cdn.net/organizations/k3g5g/square-logo/default.png': 'Secured Finance',
    'https://ethglobal.b-cdn.net/organizations/k3j5f/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/ke9sy/square-logo/default.png': 'Biconomy',
    'https://ethglobal.b-cdn.net/organizations/kkegz/square-logo/default.png': 'Superform',
    'https://ethglobal.b-cdn.net/organizations/kpdra/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/m10i3/square-logo/default.png': 'BitDSM',
    'https://ethglobal.b-cdn.net/organizations/m46sz/square-logo/default.png': 'MetaMask',
    'https://ethglobal.b-cdn.net/organizations/mba9h/square-logo/default.png': 'Flashbots',
    'https://ethglobal.b-cdn.net/organizations/mdb6w/square-logo/default.png': 'Livepeer',
    'https://ethglobal.b-cdn.net/organizations/mi9fg/square-logo/default.png': 'libp2p',
    'https://ethglobal.b-cdn.net/organizations/mj2m9/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/mnb9g/square-logo/default.png': 'Boba Network',
    'https://ethglobal.b-cdn.net/organizations/mraad/square-logo/default.png': 'XDC Foundation',
    'https://ethglobal.b-cdn.net/organizations/mt1md/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/mwuyw/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/my3b7/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/mym1p/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/mz47w/square-logo/default.png': 'Brevis',
    'https://ethglobal.b-cdn.net/organizations/na4kb/square-logo/default.png': 'Midpoint',
    'https://ethglobal.b-cdn.net/organizations/nauwe/square-logo/default.png': 'Chainsafe',
    'https://ethglobal.b-cdn.net/organizations/nbyyv/square-logo/default.png': 'XMTP',
    'https://ethglobal.b-cdn.net/organizations/nhs1x/square-logo/default.png': 'Aztec',
    'https://ethglobal.b-cdn.net/organizations/nsgxy/square-logo/default.png': 'Estuary',
    'https://ethglobal.b-cdn.net/organizations/nvm59/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/o1uf7/square-logo/default.png': 'drand',
    'https://ethglobal.b-cdn.net/organizations/o8huu/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/oa4ef/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/oiv32/square-logo/default.png': 'Aave Grants DAO',
    'https://ethglobal.b-cdn.net/organizations/omyxt/square-logo/default.png': 'Spheron',
    'https://ethglobal.b-cdn.net/organizations/op6xo/square-logo/default.png': 'DataverseOS',
    'https://ethglobal.b-cdn.net/organizations/op7tb/square-logo/default.png': 'Mona',
    'https://ethglobal.b-cdn.net/organizations/oreks/square-logo/default.png': 'Celestia',
    'https://ethglobal.b-cdn.net/organizations/owr9j/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/p7xo9/square-logo/default.png': 'Starknet',
    'https://ethglobal.b-cdn.net/organizations/pe7wh/square-logo/default.png': 'Stackr Labs',
    'https://ethglobal.b-cdn.net/organizations/pfyco/square-logo/default.png': 'The Graph',
    'https://ethglobal.b-cdn.net/organizations/pj01t/square-logo/default.png': 'Chiliz',
    'https://ethglobal.b-cdn.net/organizations/pk3b6/square-logo/default.png': 'Phala Network',
    'https://ethglobal.b-cdn.net/organizations/pn953/square-logo/default.png': 'Next.ID',
    'https://ethglobal.b-cdn.net/organizations/pxs8d/square-logo/default.png': 'Privacy + Scaling Explorations',
    'https://ethglobal.b-cdn.net/organizations/pyhsm/square-logo/default.png': 'Waku',
    'https://ethglobal.b-cdn.net/organizations/q0m99/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/q7a12/square-logo/default.png': 'Ledger',
    'https://ethglobal.b-cdn.net/organizations/qctg9/square-logo/default.png': 'Voyager',
    'https://ethglobal.b-cdn.net/organizations/qdgjh/square-logo/default.png': 'Sign Protocol',
    'https://ethglobal.b-cdn.net/organizations/qfmej/square-logo/default.png': 'Taiko',
    'https://ethglobal.b-cdn.net/organizations/qiqkw/square-logo/default.png': 'Zircuit',
    'https://ethglobal.b-cdn.net/organizations/qp08u/square-logo/default.png': 'Lattice',
    'https://ethglobal.b-cdn.net/organizations/qy8m3/square-logo/default.png': 'Polygon',
    'https://ethglobal.b-cdn.net/organizations/r3g5r/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/r7x1c/square-logo/default.png': 'Coinbase Cloud',
    'https://ethglobal.b-cdn.net/organizations/r9t85/square-logo/default.png': 'Unlock Protocol',
    'https://ethglobal.b-cdn.net/organizations/rhmm3/square-logo/default.png': 'Story Protocol',
    'https://ethglobal.b-cdn.net/organizations/ri4uk/square-logo/default.png': 'Bunzz',
    'https://ethglobal.b-cdn.net/organizations/rki5z/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/rmkrz/square-logo/default.png': 'Optimism',
    'https://ethglobal.b-cdn.net/organizations/rpgqw/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/rpi4f/square-logo/default.png': 'Coinbase Developer Platform',
    'https://ethglobal.b-cdn.net/organizations/ryn0r/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/s0vuq/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/s184f/square-logo/default.png': '0xPARC',
    'https://ethglobal.b-cdn.net/organizations/s3s6e/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/s91kj/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/sct4c/square-logo/default.png': 'Chronicle Protocol',
    'https://ethglobal.b-cdn.net/organizations/si7bt/square-logo/default.png': 'Element Finance',
    'https://ethglobal.b-cdn.net/organizations/spp1v/square-logo/default.png': 'Arbitrum',
    'https://ethglobal.b-cdn.net/organizations/sqmih/square-logo/default.png': 'Aragon',
    'https://ethglobal.b-cdn.net/organizations/szht8/square-logo/default.png': 'Streamr Network',
    'https://ethglobal.b-cdn.net/organizations/szsmr/square-logo/default.png': 'ZetaChain',
    'https://ethglobal.b-cdn.net/organizations/t3zyt/square-logo/default.png': 'ApeCoin',
    'https://ethglobal.b-cdn.net/organizations/t4bwy/square-logo/default.png': 'Lit Protocol',
    'https://ethglobal.b-cdn.net/organizations/t4tb4/square-logo/default.png': 'MakerDAO',
    'https://ethglobal.b-cdn.net/organizations/t5on2/square-logo/default.png': 'SKALE Network',
    'https://ethglobal.b-cdn.net/organizations/t6u7f/square-logo/default.png': 'Arx',
    'https://ethglobal.b-cdn.net/organizations/ta05h/square-logo/default.png': 'Gearbox',
    'https://ethglobal.b-cdn.net/organizations/tbjsr/square-logo/default.png': 'Sunscreen',
    'https://ethglobal.b-cdn.net/organizations/tff3f/square-logo/default.png': 'Airdao',
    'https://ethglobal.b-cdn.net/organizations/tw4pe/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/u0e0c/square-logo/default.png': 'Zondax',
    'https://ethglobal.b-cdn.net/organizations/u7k8j/square-logo/default.png': 'Cometh',
    'https://ethglobal.b-cdn.net/organizations/u7kt2/square-logo/default.png': 'Fuel',
    'https://ethglobal.b-cdn.net/organizations/u87dc/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/uorta/square-logo/default.png': 'IPFS',
    'https://ethglobal.b-cdn.net/organizations/uyxnw/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/v693n/square-logo/default.png': 'Huddle01',
    'https://ethglobal.b-cdn.net/organizations/v9u3u/square-logo/default.png': 'Wormhole',
    'https://ethglobal.b-cdn.net/organizations/vdiyd/square-logo/default.png': 'Alchemy',
    'https://ethglobal.b-cdn.net/organizations/vggw5/square-logo/default.png': 'Powerloom',
    'https://ethglobal.b-cdn.net/organizations/vr4u8/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/vsbye/square-logo/default.png': 'Walrus',
    'https://ethglobal.b-cdn.net/organizations/vsg6g/square-logo/default.png': 'Venn',
    'https://ethglobal.b-cdn.net/organizations/vsqgj/square-logo/default.png': 'EY Blockchain',
    'https://ethglobal.b-cdn.net/organizations/vxwti/square-logo/default.png': 'Lens Protocol',
    'https://ethglobal.b-cdn.net/organizations/vy7pe/square-logo/default.png': 'Morph',
    'https://ethglobal.b-cdn.net/organizations/w1nth/square-logo/default.png': 'Kinto',
    'https://ethglobal.b-cdn.net/organizations/w1xgi/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/w9gtd/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/wb7qe/square-logo/default.png': 'Router',
    'https://ethglobal.b-cdn.net/organizations/wdteq/square-logo/default.png': 'Circles',
    'https://ethglobal.b-cdn.net/organizations/weaax/square-logo/default.png': 'Safe',
    'https://ethglobal.b-cdn.net/organizations/wuc6g/square-logo/default.png': 'Etherspot',
    'https://ethglobal.b-cdn.net/organizations/x2bo0/square-logo/default.png': 'Lighthouse',
    'https://ethglobal.b-cdn.net/organizations/x3xey/square-logo/default.png': 'Circle',
    'https://ethglobal.b-cdn.net/organizations/x566a/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/x59d1/square-logo/default.png': 'Superfluid',
    'https://ethglobal.b-cdn.net/organizations/x6m3m/square-logo/default.png': 'Tellor',
    'https://ethglobal.b-cdn.net/organizations/xdat5/square-logo/default.png': 'Finalist',
    'https://ethglobal.b-cdn.net/organizations/xefox/square-logo/default.png': 'Valist',
    'https://ethglobal.b-cdn.net/organizations/xf84v/square-logo/default.png': 'Empiric',
    'https://ethglobal.b-cdn.net/organizations/xrzks/square-logo/default.png': 'Dynamic',
    'https://ethglobal.b-cdn.net/organizations/y24y0/square-logo/default.png': 'zkSync',
    'https://ethglobal.b-cdn.net/organizations/y4cxw/square-logo/default.png': 'Dfns',
    'https://ethglobal.b-cdn.net/organizations/y6na5/square-logo/default.png': 'SSV Network',
    'https://ethglobal.b-cdn.net/organizations/y6rde/square-logo/default.png': 'CoopHive',
    'https://ethglobal.b-cdn.net/organizations/y9b9g/square-logo/default.png': 'Openmesh Network',
    'https://ethglobal.b-cdn.net/organizations/ygz83/square-logo/default.png': 'Connext',
    'https://ethglobal.b-cdn.net/organizations/yip67/square-logo/default.png': 'Scroll',
    'https://ethglobal.b-cdn.net/organizations/ypbun/square-logo/default.png': 'Envio',
    'https://ethglobal.b-cdn.net/organizations/yrwii/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/yuvir/square-logo/default.png': 'Euler',
    'https://ethglobal.b-cdn.net/organizations/z95d6/square-logo/default.png': 'SSV Network',
    'https://ethglobal.b-cdn.net/organizations/z9n70/square-logo/default.png': 'Bitkub',
    'https://ethglobal.b-cdn.net/organizations/zerib/square-logo/default.png': 'frames.js',
    'https://ethglobal.b-cdn.net/organizations/zhkg5/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/zjspv/square-logo/default.png': '???',
    'https://ethglobal.b-cdn.net/organizations/zxd3n/square-logo/default.png': 'Web3Auth',
}

from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# # Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_service_key = os.getenv("SUPABASE_SERVICE_KEY")
supabase = create_client(supabase_url, supabase_service_key)

# Prepare data for insertion
prize_data = [
    {"name": name, "img_url": url}
    for url, name in imageUrls.items()
]

# Upload to Supabase
try:
    response = supabase.table("prizes").insert(prize_data).execute()
    print(f"Successfully uploaded {len(prize_data)} records")
except Exception as e:
    print(f"Error uploading to Supabase: {e}")